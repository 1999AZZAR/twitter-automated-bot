# Twitter Video Uploader

This Python code allows you to upload videos to Twitter using the Twitter API. The code uses the OAuth1 authentication flow and provides a `VideoTweet` class that handles the video uploading process.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system
- Requests library installed (`pip install requests`)
- Requests-OAuthlib library installed (`pip install requests_oauthlib`)
- Twitter API credentials (consumer key, consumer secret, access key, and access secret)

## Getting Started

1. Clone or download the code repository to your local machine.
2. Open the code file (`twitter_video_uploader.py`) in a text editor or Python IDE.
3. Replace the placeholder values in the `constants.py` file with your actual Twitter API credentials.
4. Set the `VIDEO_FILENAME` variable to the path of the video file you want to upload.
5. Save the changes to the `constants.py` file.

## Usage

1. Import the `VideoTweet` class from the `twitter_video_uploader` module into your own Python script.
2. Create an instance of the `VideoTweet` class, providing the path to the video file as an argument.
3. Use the instance to upload the video and post a tweet with the video.

## Example Usage

```python
from twitter_video_uploader import VideoTweet

# Create an instance of the VideoTweet class
video_uploader = VideoTweet('path/to/video/file.mp4')

# Upload the video to Twitter
video_uploader.upload_init()
video_uploader.upload_append()
video_uploader.upload_finalize()

# Post a tweet with the uploaded video
tweet_text = "Check out this video!"
video_uploader.tweet(tweet_text)
```

## Class Methods

### `__init__`

- Initializes the `VideoTweet` object with the path to the video file.

### `upload_init`

- Initializes the video upload process by sending an INIT request to the Twitter API.
- Retrieves the media ID for the video.

### `upload_append`

- Uploads the video file in chunks by sending APPEND requests to the Twitter API.
- Appends each chunk of the video file to the media upload.

### `upload_finalize`

- Finalizes the video upload process by sending a FINALIZE request to the Twitter API.
- Starts the video processing.

### `check_status`

- Checks the status of the video processing.
- Waits for the processing to complete before proceeding.

### `tweet`

- Posts a tweet with the uploaded video by sending a request to the Twitter API.
- Associates the media ID with the tweet.

## Notes

- Make sure you handle exceptions appropriately when using the `VideoTweet` class methods to handle errors and avoid unexpected behavior.
- Ensure that you comply with Twitter's API usage policies and terms of service when using this code.

Feel free to explore and modify the code to suit your specific requirements. If you have any questions or encounter any issues, please don't hesitate to ask for assistance. Happy video uploading on Twitter!
