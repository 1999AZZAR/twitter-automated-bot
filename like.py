import tweepy
from time import sleep
from twitter import Twitter
from tweepy import api
from constants import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SCRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tw = Twitter()

for tweet in tweepy.Cursor(api.search,q=('#lamongan' or '#lamonganmegilan' or '#beritalamongan'),).items(10):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.favorite()
        print('Like the tweet')
        sleep(25)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
