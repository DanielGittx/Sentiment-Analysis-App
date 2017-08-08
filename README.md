# Safaricom_social_tracker_application
Socio-Tracker

This is an application that uses machine-learning to monitor people's attitude in social media (twitter) towards a product or topic in debate as positive or negative.


SOFTWARE ARCHITECTURAL CONSIDERATIONS:-

Handling over 1M users - Scalability is one of the most important aspect in design of modern software architectures. Below are some techniques to ensure that the system is scalable:- a. Three tier approach that involves:- * The client tier - responsible for interacting with the user via a Graphical User Interface (GUI) and submitting requests via the network to the mid tier. Use of Html and Javascript charts to submit requests and render results respecively. * The mid-tier - responsible for gathering requests from clients and executing transactions against the data tier. Use of JavaScript Object Notation (JSON). * The data tier - responsible for physical storage and manipulation of the information represented by application queries and the responses to those queries. Use of a relational database engine (e.g MYSQL) b. Service Oriented approach:- This involves decoupling of functionality; grouping of components into "areas of concern". Different functionalities/contexts interact with each other through abstract interface. In this design the different components are contextualized through pickling (creating pickles).

Concurrency:- This is where several computations are executed during overlapping time periods. In this case use of thread-safe structures is adopted.

High I/O:- In this project, word tokenization and speech tagging is utilized. This involves breaking of sentences into words and classifying the according to their respective parts of speech; only adjectives are used to determine the sentiment/attitude.

Utilization of front end and Backend.
- Limited Front end development in Html and Javascript.
- Backend - Python is used in the backend. As different tasks are contextualized, most variables are local variables.
- python accesses local variables more efficiently than global variables. Also use of looping structures to loop over a sequence of words in sentences.
- Python was also preferred as its machine learning libraries and community community is more developed/wide.


SUMMARY NOTES FOR THE FILES AND METHODS IN THIS PROJECT:-
1. main.py
* Training set of data is loaded into application from positive.txt and negative.txt
* Named entity recognition/speech tagging is done through the use of adjectives to generates the word features dictionary.
  The word features dictionary is used to categorize input data(tweets) for classification.
* Pickling:- Serializing of object structures for faster access in future.
* Features (negative/positive) are shuffled toavoid bias during classification.
* Classification Accuracy:- These text classifiers below are used and their accuracy value returned.
			          MNB_classifier,
                                  LogisticRegression_classifier,
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  SGDClassifier_classifier
*Voted Classifier:- The method sentiment() returns 1. sentiment_value (as positive or negative)
					           2. confidence (in percentage; how positive/negative a sentiment is)


2. plottingLiveData.py
* Logic to read positives/negatives results to determine x and y axes for graphing
* Results from custom functions and public API are plotted together to avail even more accurate confidence review
* Use of ggplot to render sentiment graph


3. testfile.py
* Logic to read positives/negatives results to determine x and y axes for graphing
* Attempted use of Hiharts and JavaScript to render sentiment graph in a browser

4. twitterLiveStream.py
* This file contains public API's (twitter API and Open Calais API by Reuters)
* Twitter API is used to stream live data from twitter which is passed though local/custom classifiers (main.py) and Open Calais API for language processing.]
* Only confidence level above 70% is accepted and saved ina text file (twitter_results_to_plot.txt) for graphical rendering.
*


