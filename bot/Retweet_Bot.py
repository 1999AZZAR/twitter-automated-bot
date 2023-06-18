import tweepy
import time
from twitter import Twitter
from constants import *

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SCRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tw = Twitter()

# Search for tweets and retweet them
for tweet in tweepy.Cursor(api.search, q='#lamongan OR #lamonganmegilan OR #beritalamongan').items(20):
    try:
        print('\nbot found tweet by @' + tweet.user.screen_name)
        tweet.retweet()
        print('retweet successful.')
        time.sleep(25) # Wait for 25 seconds before retweeting the next tweet
    except tweepy.TweepError as error:
        print('\nError: Retweet not successful. Reason: ' + error.reason)
        continue
