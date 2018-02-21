import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features
import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = "t5dtLp62IUNrMlfHyLxFpEt4A"
consumer_secret = "Com6dxqLjaJsoG1AzOjfuHvvckUPnzOuHcTbkOanxFbDKrJX4G"
access_token = "2326387646-XfKBz1wcb0V7oHbitZNdhnghxsBT4kBIz1CG0qk"
access_token_secret = "UMp1uWuowEgfPRe9aCV9zAEwqQIRD4TZs2qI3LxEbgmjE"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
popTweets = {}
popTweetIndex = 0;

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
for status in tweepy.Cursor(api.search, q='bitcoin -filter:retweets -filter:links', lang='en').items(200):
    popTweets[popTweetIndex] = status.text
    popTweetIndex += 1

trendString = ''

for i in range(0, popTweets.__len__()):
    trendString += popTweets[i]
    print(popTweets[i])

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='1b4fdeab-97f9-47c1-950e-24df1753535f',
    password='6CXj72fTSG0W')

response = natural_language_understanding.analyze(
    text=trendString,
    features=[Features.Sentiment(), Features.Emotion()])

print(json.dumps(response, indent=2))