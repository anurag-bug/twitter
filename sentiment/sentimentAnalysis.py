import sys,tweepy,csv,re
from textblob import TextBlob
from . import models
class Analysis:
    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self,searchTerm,NoOfTerms):
        # authenticating
        consumerKey = 'K3QBlgCPNL6gzMtEE4tPdSBKg'
        consumerSecret = 'fgCOmIcBGe1KP4zw5JJVepUiJrs3CcAOjNnQVTWpu0iFNoWHVK'
        accessToken = '834397594944053249-41fRRVSDB1RnDIya4H9gexlTf0OfwW6'
        accessTokenSecret = 'tzGao8QrxFIpVv1etjkcrYM6JP4CYFEPCIqJ1Rl81vG0T'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        # input for term to be searched and how many tweets to search

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

        # Open/create a file to append data to
        csvFile = open('result.csv', 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)


        # creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0


        # iterating through tweets fetched
        models.positiveTweets.objects.all().delete()
        models.negativeTweets.objects.all().delete()
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            #print (tweet.text)    #print tweet's text
            analysis = TextBlob(self.removeURL(tweet.text))
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later
            if (analysis.sentiment.polarity>0):
                tweetObject=models.positiveTweets()
                tweetObject.tweetText=tweet.text
                tweetObject.user=str(tweet.user.name)
                tweetObject.time=tweet.created_at
                tweetObject.save()
            if (analysis.sentiment.polarity<0):
                tweetObject=models.negativeTweets()
                tweetObject.tweetText=tweet.text
                tweetObject.user=str(tweet.user.name)
                tweetObject.time=tweet.created_at
                tweetObject.save()
            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1
        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        return {'positive':positive,'wpositive':wpositive,'spositive':spositive,'negative':negative,
                'wnegative':wnegative,'snegative':snegative,'neutral':neutral}

    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def removeURL(self,string):
        mylist=string.split()
        mystr=""
        for i in mylist:
            if len(i)>4 and i[0:4]=="http":
                continue
            else:
                mystr=mystr+i+" "
        return mystr

