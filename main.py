import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, NuSVC, LinearSVC
import pickle
import csv
import codecs

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize, sent_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


short_pos = open("short_reviews/positive.txt", "r").read()   #Load Training text
short_neg = open("short_reviews/negative.txt", "r").read()


all_words = []
documents = []


# J is adjective, R is adverb, and V is verb
# allowed_word_type = ["J", "R, "V]
allowed_word_type = ["J"]

for p in short_pos.split('\n'):
    documents.append((p, "pos"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_type:
            all_words.append(w[0].lower())


for p in short_neg.split('\n'):
    documents.append((p, "neg"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_type:
            all_words.append(w[0].lower())

open_file = open("pickle_Algorithms/documents.pickle", "rb")
documents = pickle.load(open_file)
open_file.close()
#########################################################################################################

all_words = nltk.FreqDist(all_words)


word_features = list(all_words.keys())[:5000] #we want to use the most common 5000 words only


open_file = open("pickle_Algorithms/word_features.pickle", "rb")
word_features = pickle.load(open_file)
open_file.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


featuresets = [(find_features(rev), category) for (rev, category) in documents]
# training / testing set

random.shuffle(featuresets)
print(len(featuresets))

#Positive/Negative Data shuffled
training_set = featuresets[:10000] #Everyrthing upto 10000
testing_set = featuresets[10000:]  #Everuithong beyond 10000

#Negative Data
#training_set = featuresets[100:]
#testing_set = featuresets[:100]

####################################################################################################################
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes_Classifier Accuracy %", (nltk.classify.accuracy(classifier, testing_set))*100)
#classifier.show_most_informative_features(15)

open_file = open("pickle_Algorithms/Original_Naive_Bayes_Classifier.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()
###################################################################################################################

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_Classifier Accuracy %", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

open_file = open("pickle_Algorithms/MultinomialNB_Classifier.pickle", "rb")
MNB_classifier = pickle.load(open_file)
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_Classifier Accuracy %", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

open_file.close()

#GaussianNB_classifier = SklearnClassifier(GaussianNB())
#GaussianNB_classifier.train(training_set)
#print("GaussianNB_classifier Accuracy %", (nltk.classify.accuracy(GaussianNB_classifier,testing_set))*100)
#####################################################################################################################

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_Classifier Accuracy %", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

open_file = open("pickle_Algorithms/BernoulliNB_Classifier.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()
#####################################################################################################################


open_file = open("pickle_Algorithms/LogisticRegression_Classifier.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()
##############################################################################################################################

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_Classifier Accuracy %", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

open_file = open("pickle_Algorithms/SGD_Classifier.pickle", "rb")
SGDClassifier_classifier = pickle.load(open_file)
open_file.close()
##################################################################################################################################
##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(training_set)
##print("SVC_Classifier Accuracy %", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_Classifier Accuracy %", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

open_file = open("pickle_Algorithms/NuSVC_Classifier.pickle", "rb")
NuSVC_classifier = pickle.load(open_file)
open_file.close()
##################################################################################################################################

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_Classifier Accuracy %", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

open_file = open("pickle_Algorithms/LinearSVC_Classifier.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()
##################################################################################################################################

voted_classifier = VoteClassifier(classifier,
                                  BernoulliNB_classifier,
                                  MNB_classifier,
                                  LogisticRegression_classifier,
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  SGDClassifier_classifier)

print("voted_classifier Accuracy %", (nltk.classify.accuracy(voted_classifier, testing_set))*100)


#print ("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %", voted_classifier.confidence(testing_set[0][0])*100)
#print ("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %", voted_classifier.confidence(testing_set[1][0])*100)
#print ("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %", voted_classifier.confidence(testing_set[2][0])*100)
#print ("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %", voted_classifier.confidence(testing_set[3][0])*100)
#print ("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %", voted_classifier.confidence(testing_set[4][0])*100)
#print ("Classification:", voted_classifier.classify(testing_set[5][0]), "Confidence %", voted_classifier.confidence(testing_set[5][0])*100)

def sentiment(text):
    feats = find_features(text)

    return voted_classifier.classify(feats), voted_classifier.confidence(feats)


