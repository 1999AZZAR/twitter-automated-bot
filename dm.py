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
                        if dm['media'] == None:
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
