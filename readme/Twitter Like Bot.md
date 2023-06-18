# Twitter Like Bot

This Python script allows you to create a bot that searches for tweets based on a specific search query and automatically likes them using the Twitter API. The code utilizes the Tweepy library to interact with the Twitter API for authentication and like functionality.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system
- Tweepy library installed (`pip install tweepy`)
- Twitter API credentials (consumer key, consumer secret, access key, and access secret)
- Custom `twitter.py` file containing the `Twitter` class and its methods
- Custom `constants.py` file containing the Twitter API credentials

## Getting Started

1. Clone or download the code repository to your local machine.
2. Open the code file (`like_bot.py`) in a text editor or Python IDE.
3. Replace the placeholder values in the `constants.py` file with your actual Twitter API credentials.
4. Save the changes to the `constants.py` file.
5. Import the `Twitter` class from the `twitter` module into the `like_bot.py` script.
6. Authenticate with the Twitter API by creating an instance of `tweepy.OAuthHandler` and setting the access token.
7. Create an instance of the `Twitter` class to handle interactions with the Twitter API.

## Usage

1. Customize the search query by modifying the `search_query` variable in the script. You can update the hashtags or keywords to search for relevant tweets.
2. Adjust the maximum number of tweets to like by modifying the `max_tweets` variable. The code currently likes up to 10 tweets.
3. Run the `like_bot.py` script.
4. The bot will search for tweets matching the specified search query and like them using the `api.create_favorite` method provided by Tweepy.
5. After liking a tweet, the bot will wait for 25 seconds before liking the next tweet.
6. If an error occurs during the liking process, the bot will print the error message and continue to the next tweet.

## Example Usage

```python
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
```

## How it Works

1. The script authenticates with the Twitter API using the provided API credentials.
2. An instance of the `Twitter` class is created to handle interactions with the Twitter API for liking functionality.
3. The script uses the Tweepy library to search for tweets based on the specified search query using the `api.search` method.
4. It retrieves up to the specified number of tweets (10 in the example) using the `items()` parameter of `tweepy.Cursor`.
5. For each tweet found, the script attempts to like it using the `api.create_favorite` method provided by Tweepy.
6. After liking a tweet, the script waits for 25 seconds before liking the next tweet.
7. If an error occurs during the liking process (such as reaching the rate limit), the script prints the error message and continues to the next tweet.
8. The script will exit when it has liked the maximum number of tweets specified or when there are no more tweets matching the search query.

Please note that while the code provides a basic structure for creating a Twitter like bot, it's essential to review and comply with Twitter's API usage policies and terms of service. Additionally, ensure that your bot's actions align with Twitter's guidelines and do not violate any rules or regulations.

Feel free to modify and enhance the code according to your specific requirements. If you have any questions or encounter any issues, feel free to reach out for assistance. Happy liking!
