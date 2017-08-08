from tweepy import Stream
from tweepy import OAuthHandler                      # No need to PIP THIS!!!!!!!!!!!!!!!
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json
import urllib,urllib2
import sys
import main as m   # The function sentiment() in main.py returns sentiment_value and confidence

#Database config to save different users inputs/requests
                        #server,    MySQL username, mysql pwd, Database_name
conn = MySQLdb.connect("localhost", "useraccount", "saf_proj", "twitterfeedDB")
c = conn.cursor()

#Twitter API AUTHENTICATION
#consumer key, consumer secret, access token, access secret
#Authentication and authorisation to the public API

ckey = "UcRP1JNvVEk5AFQJ3kdc5u4BH"
csecret = "vkaFXRo0a4lIhxHP3FVpVZfrV0Ljk9UEwp9wBQW5Xzuo6bMgj7"
atoken = "745559408101433344-Pc8NDKQFyZx6I5CY8SGu3240h4QXbxY"
asecret = "42mQp7RDMsH4F5Ou4QaBmO8LKGRX5s74FUID1bkAgUCTj"


##OPEN CALAIS API
def Sent_Analysis_from_calais(text):

    ##### set API key and REST URL values.

    x_ag_access_token1 = 'O7tTcXv6TFHA4Z5EKjjxPcrcdWndxl'  # your Calais API key.
    calaisREST_URL = 'https://api.thomsonreuters.com/permid/Calais'  # REST interface.
    # info on the newer one: http://www.opencalais.com/documentation/calais-web-service-api/api-invocation/rest
    # alert user and shut down if the API key variable is still null.
    if x_ag_access_token1 == '':
        print "You need to set your Calais API key in the 'x_ag_access_token' variable."
    sys.exit()
    ## set the text to ask Calais to analyze.
    sampleText = text

    ##### set XML parameters for Calais.

    # see "Input Parameters" at: http://www.opencalais.com/documentation/calais-web-service-api/forming-api-calls/input-parameters
    calaisParams = '''
    <c:params xmlns:c="http://s.opencalais.com/1/pred/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
     <c:processingDirectives c:contentType="text/txt"
      c:enableMetadataType="GenericRelations,SocialTags"
      c:outputFormat="Text/Simple"/>
     <c:userDirectives/>
     <c:externalMetadata/>
    </c:params>
    '''

    ## send data to Calais API.

    # see: http://www.opencalais.com/APICalls
    dataToSend = urllib.urlencode({
        'x-ag-access-token': x_ag_access_token1,
        'content': sampleText,
        'paramsXML': calaisParams
    })
    ##### get API results  .
    results_calais = urllib2.urlopen(calaisREST_URL, dataToSend).read()
    return results_calais


class listener(StreamListener):
    def on_data(self,data):
        try:
            ## Public API analysis
            tweet = data.split(',"text":')[1].split('","source')[0]
            sentiment_rating = Sent_Analysis_from_calais(tweet)              #Just save this result ina a .txt. could also be saved in db
            save_rating_doc = tweet + '::' + sentiment_rating + '\n'
            if sentiment_rating >= 70:
               output = open('output_Calais.txt','a')
               output.write(save_rating_doc)
               output.close()

            ##Just save tweets but we need to delete them before 24hrs!
            all_data = json.loads(data)
            tweet = all_data["text"]
            username = all_data["user"]["screen_name"]
            c.execute("INSERT INTO Users_Table (time,username,tweet) VALUES (%S,%S,%S)",
                      (time.time(),username,tweet))
            conn.commit()
            print((username,tweet))
            #print((tweet))

            sentiment_value, confidence = m.sentiment(tweet)
            print (tweet, sentiment_value,confidence)

            if confidence*100 >= 70:              #This is aggregate/overall confidence level as reported by classifiers used
                output = open("twitter_results_to_plot.txt", "a")      #The confidence level above is saved in a text file
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["safaricom blaze"])   #"key word" or "search topic"








