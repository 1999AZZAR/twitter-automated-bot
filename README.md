# Twitter Automation bot (scripts)

This repository contains Python scripts for automating various tasks on Twitter using the Twitter API. Each script focuses on a specific functionality and utilizes the Tweepy library to interact with the Twitter API.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system
- Tweepy library installed (`pip install tweepy`)
- Twitter API credentials (consumer key, consumer secret, access key, and access secret)

## Getting Started

1. Clone or download the code repository to your local machine.
2. Open the desired code file in a text editor or Python IDE.
3. Replace the placeholder values in the `constants.py` file with your actual Twitter API credentials.
4. Save the changes to the `constants.py` file.

## Scripts

### 1. Twitter Video Uploader

- Description: This Python code allows you to upload videos to Twitter using the Twitter API. The code uses the OAuth1 authentication flow and provides a `VideoTweet` class that handles the video uploading process.
- File: [`video_uploader.py`](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/bot/Video_Uploader.py)
- [Explanation](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/readme/Twitter%20Video%20Uploader.md)

### 2. Twitter Retweet Bot

- Description: This Python script allows you to create a bot that searches for tweets based on specific hashtags and automatically retweets them using the Twitter API. The code utilizes the Tweepy library for authentication and retweet functionality.
- File: [`retweet_bot.py`](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/bot/Retweet_Bot.py)
- [Explanation](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/readme/Twitter%20Retweet%20Bot.md)

### 3. Twitter Like Bot

- Description: This Python script allows you to create a bot that searches for tweets based on a specific search query and automatically likes them using the Twitter API. The code utilizes the Tweepy library for authentication and like functionality.
- File: [`like_bot.py`](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/bot/Like_Bot.py)
- [Explanation](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/readme/Twitter%20Like%20Bot.md)

### 4. Twitter Direct Message Processor

- Description: This Python script allows you to process direct messages (DMs) on Twitter using the Twitter API. The code utilizes the `Twitter` class from the `twitter` module to interact with the Twitter API and perform actions such as reading DMs, posting tweets, and deleting DMs.
- File: [`dm_processor.py`](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/bot/DM_Processor.py)
- [Explanation](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/readme/Twitter%20Direct%20Message%20Processor.md)

### 5. Twitter Media Upload Bot

- Description: This Python script allows you to create a bot that uploads images or videos to Twitter using the Twitter API. The code utilizes the Tweepy library for authentication and media upload functionality. The script provides a `MediaUploadBot` class that handles the media uploading process.
- File: [`twitter_bot.py`](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/bot/Twitter_Bot.py)
- [Explanation](https://github.com/1999AZZAR/twitter-automated-bot/blob/main/readme/Twitter%20Bot%20with%20Media%20Upload.md)

## Usage

- Each script provides detailed instructions on how to use it effectively. Please refer to the specific script's documentation for usage guidelines and examples.

## Notes

- Make sure you handle exceptions appropriately when using the provided scripts to handle errors and avoid unexpected behavior.
- Ensure that you comply with Twitter's API usage policies and terms of service when using these scripts.

Feel free to explore and modify the code to suit your specific requirements. If you have any questions or encounter any issues, please don't hesitate to ask for assistance. Happy automating on Twitter!
