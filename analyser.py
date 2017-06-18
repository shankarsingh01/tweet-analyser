import tweepy
from textblob import TextBlob

#TwitterAPI
consumerKey= ''
consumerSecret= ''

accessToken=''
accessTokenSecret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Search
public_tweets = api.search('isis')





count=0
pos=0
neg=0
neutral=0
for tweet in public_tweets:
    print(tweet.text)
    #Count Variable
    count+=1
    
    analysis = TextBlob(tweet.text)
    if(analysis.sentiment.polarity<0):
    	neg+=1
    elif(analysis.sentiment.polarity>0):
    	pos+=1
    elif(analysis.sentiment.polarity==0):
    	neutral+=1

print("Neutral",(neutral/count) * 100 )
print("Positive",(pos/count) * 100 )
print("Negative",(neg/count)*100)

    
