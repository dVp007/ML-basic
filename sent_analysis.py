# rplace consumer key ,consumer secret, access token,access token secret
# credits siraj raval

import tweepy
from textblob import TextBlob

ck ="consumer key"
cs = "consumer secret"

at = "access token"
ats = "access token secret"

auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at,ats)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for t in public_tweets:
	print(t.text.encode('utf-8'))
	analy = TextBlob(t.text)
	print(analy.sentiment)