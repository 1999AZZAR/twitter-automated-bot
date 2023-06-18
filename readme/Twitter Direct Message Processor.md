# Twitter Direct Message Processor

This Python script allows you to process direct messages (DMs) on Twitter using the Twitter API. The code utilizes the `Twitter` class from the `twitter` module to interact with the Twitter API and perform actions such as reading DMs, posting tweets, and deleting DMs.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system
- Tweepy library installed (`pip install tweepy`)
- Twitter API credentials (consumer key, consumer secret, access key, and access secret)

## Getting Started

1. Clone or download the code repository to your local machine.
2. Open the code file (`dm_processor.py`) in a text editor or Python IDE.
3. Replace the placeholder values in the `twitter.py` file with your actual Twitter API credentials.
4. Save the changes to the `twitter.py` file.

## Usage

1. Import the `Twitter` class from the `twitter` module into your own Python script.
2. Create an instance of the `Twitter` class.
3. Use the instance to process direct messages.

## Example Usage

```python
from twitter import Twitter
import time

tw = Twitter()


def dm():
    print("Starting program...")
    while True:
        dms = tw.read_dm()
        if len(dms) != 0:
            for dm in dms:
                message = dm['message']
                sender_id = dm['sender_id']
                dm_id = dm['id']
                if len(message) != 0 and len(message) < 280 and ("lurr" in message.lower()):
                    message = message.replace("lurr", "")
                    if len(message) != 0:
                        if dm['media'] is None:
                            print("DM will be posted")
                            tw.post_tweet(message)
                            tw.delete_dm(dm_id)
                        else:
                            print("DM will be posted with media")
                            print(dm['shorted_media_url'])
                            tw.post_tweet_with_media(
                                message, dm['media'],
                                dm['shorted_media_url'],
                                dm['type'])
                            tw.delete_dm(dm_id)
                    else:
                        print("DM deleted because it is empty..")
                        tw.delete_dm(dm_id)
                else:
                    print("DM will be deleted because it does not contain the keyword..")
                    tw.delete_dm(dm_id)
        else:
            print("Direct message is empty...")
            time.sleep(50)


if __name__ == "__main__":
    dm()
```

## How it Works

1. The script creates an instance of the `Twitter` class, which handles interactions with the Twitter API.
2. The `dm()` function is the main entry point of the script and contains the logic for processing DMs.
3. The function continuously checks for new DMs by calling the `read_dm()` method of the `Twitter` class.
4. If there are any DMs, the function iterates over each DM and checks if it meets the required criteria.
5. If a DM contains a non-empty message with a length less than 280 characters and the keyword "lurr" (case-insensitive), further processing is performed.
6. If the DM does not contain the keyword or the message is empty, the DM is deleted using the `delete_dm()` method of the `Twitter` class.
7. If the DM meets the criteria, it is either posted as a tweet (text only) using the `post_tweet()` method or posted as a tweet with media (photo or video) using the `post_tweet_with_media()` method.
8. After the DM is processed, it is deleted using the `delete_dm()` method.
9. If there are no DMs, the script waits for 50 seconds before checking again.

Note: Make sure you handle exceptions appropriately when using the `Twitter` class methods to handle errors and avoid unexpected behavior. Ensure that you comply with Twitter's API usage policies and terms of service when using this code.

Feel free to explore and modify the code to suit your specific requirements. If you have any questions or encounter any issues, please don't hesitate to ask for assistance. Happy processing of DMs on Twitter!
