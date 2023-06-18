import tweepy
from time import sleep
from twitter import Twitter
from constants import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SCRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tw = Twitter()

search_query = '#lamongan OR #lamonganmegilan OR #beritalamongan'
max_tweets = 10

for tweet in tweepy.Cursor(api.search, q=search_query).items(max_tweets):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        api.create_favorite(tweet.id)
        print('Liked the tweet')
        sleep(25)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
