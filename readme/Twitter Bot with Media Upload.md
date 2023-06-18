# Twitter Bot with Media Upload

This Python code provides a Twitter bot class that allows you to perform various actions on Twitter, including reading direct messages, posting tweets, and uploading media (photos and videos) to your Twitter account. The bot utilizes the Tweepy library and Twitter API for communication.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system
- Tweepy library installed (`pip install tweepy`)
- Twitter API credentials (consumer key, consumer secret, access key, and access secret)

## Getting Started

1. Clone or download the code repository to your local machine.
2. Open the code file (`twitter_bot.py`) in a text editor or Python IDE.
3. Replace the placeholder values in the `constants.py` file with your actual Twitter API credentials.
4. Save the changes to the `constants.py` file.

## Usage

1. Import the `Twitter` class from the `twitter_bot` module into your own Python script.
2. Create an instance of the `Twitter` class.
3. Use the instance to perform the desired actions on Twitter.

## Example Usage

```python
from twitter_bot import Twitter

# Create an instance of the Twitter bot
bot = Twitter()

# Read direct messages
direct_messages = bot.read_dm()
for dm in direct_messages:
    # Process each direct message

    # Delete a direct message
    bot.delete_dm(dm['id'])

# Post a tweet
tweet_text = "Hello, Twitter!"
bot.post_tweet(tweet_text)

# Post a tweet with media (photo or video)
tweet_with_media = "Check out this photo! #photooftheday"
media_url = "https://example.com/photo.jpg"
shorted_media_url = "https://t.co/abcxyz"
media_type = "photo"
bot.post_tweet_with_media(tweet_with_media, media_url, shorted_media_url, media_type)
```

## Class Methods

### `__init__`

- Initializes the Twitter bot with the provided Twitter API credentials.

### `read_dm`

- Retrieves and returns a list of direct messages received by the bot.
- The method returns a list of dictionaries, where each dictionary represents a direct message and contains information such as the message text, sender ID, message ID, media URL (if present), and media type.

### `delete_dm`

- Deletes a direct message with the specified message ID.

### `post_tweet`

- Posts a tweet with the provided text.

### `post_tweet_with_media`

- Posts a tweet with the provided text and media (photo or video).
- The method downloads the media from the provided URL and uploads it to Twitter before posting the tweet.

## Notes

- Make sure you handle exceptions appropriately when using the Twitter bot methods to handle errors and avoid unexpected behavior.
- Ensure that you comply with Twitter's API usage policies and terms of service when using this code.

Feel free to explore and modify the code to suit your specific requirements. If you have any questions or encounter any issues, please don't hesitate to ask for assistance. Happy tweeting!
