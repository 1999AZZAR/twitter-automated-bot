from twitter import Twitter
import time

tw = Twitter()


def dm():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) != 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']
                if len(message) != 0 and len(message) < 280:
                    if "lurr" or "Lurr" or "LURR" in message:
                        message = message.replace("lurr" or "Lurr" or "LURR"," ")
                        if len(message) != 0:
                            if dms[i]['media'] == None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(
                                    message, dms[i]['media'],
                                    dms[i]['shorted_media_url'],
                                    dms[i]['type'])
                                tw.delete_dm(id)
                        else:
                            print("DM deleted because its empty..")
                            tw.delete_dm(id)
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        tw.delete_dm(id)
            dms = list()
        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) == 0 or dms == None:
                time.sleep(50)
if __name__ == "__main__":
    dm()
