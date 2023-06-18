# Twitter Retweet Bot

This Python script allows you to create a bot that searches for tweets based on specific hashtags and automatically retweets them using the Twitter API. The code utilizes the Tweepy library to interact with the Twitter API for authentication and retweet functionality.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system
- Tweepy library installed (`pip install tweepy`)
- Twitter API credentials (consumer key, consumer secret, access key, and access secret)
- Custom `twitter.py` file containing the `Twitter` class and its methods
- Custom `constants.py` file containing the Twitter API credentials

## Getting Started

1. Clone or download the code repository to your local machine.
2. Open the code file (`retweet_bot.py`) in a text editor or Python IDE.
3. Replace the placeholder values in the `constants.py` file with your actual Twitter API credentials.
4. Save the changes to the `constants.py` file.
5. Import the `Twitter` class from the `twitter` module into the `retweet_bot.py` script.
6. Authenticate with the Twitter API by creating an instance of `tweepy.OAuthHandler` and setting the access token.
7. Create an instance of the `Twitter` class to handle interactions with the Twitter API.

## Usage

1. Customize the search query by modifying the `q` parameter in the `tweepy.Cursor` line. You can update the hashtags or keywords to search for tweets.
2. Adjust the number of tweets to retweet by modifying the `items()` parameter. The code currently retweets 20 tweets.
3. Run the `retweet_bot.py` script.
4. The bot will search for tweets matching the specified hashtags, retweet them, and wait for 25 seconds before retweeting the next tweet.
5. If an error occurs during retweeting, the bot will continue to search and retweet other tweets.

## Example Usage

```python
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
```

## How it Works

1. The script authenticates with the Twitter API using the provided API credentials.
2. An instance of the `Twitter` class is created to handle interactions with the Twitter API for retweeting functionality.
3. The script uses the Tweepy library to search for tweets based on the specified hashtags using the `api.search` method.
4. It retrieves the specified number of tweets (20 in the example) using the `items()` parameter of `tweepy.Cursor`.
5. For each tweet found, the script attempts to retweet it using the `tweet.retweet()` method provided by Tweepy.
6. If the retweet is successful, it waits for 25 seconds (adjustable) before retweeting the next tweet.
7. If an error occurs during retweeting (such as duplicate retweets), the script catches the exception and continues to the next tweet.

Please note that this code is intended as a starting point for building a Twitter retweet bot. Make sure to comply with Twitter's API usage policies and terms of service, and consider adding additional features or error handling based on your specific requirements.

Feel free to explore and modify the code to suit your needs. If you have any questions or run into any issues, please don't hesitate to ask for assistance. Happy retweeting!
