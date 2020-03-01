from bots.config_app import create_api
import tweepy
import logging
import time
from tweepy import Cursor
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

beginning = ["Hey ", "Hi ", "Hello ", "Greetings, "]
replies = ["Mr. Stark would like you to resume Studying",
           "I think it's your time to study, Mr. Stark will get in touch with you soon!",
           "I am here to remind you that you should be studying! Mr. Stark has your best interests at heart!",
           "It's me again! Mr. Stark told me to remind you that you should not be wasting your time on twitter!"]


def generate_reply(item):
    begin_response = random.randrange(0, 4)
    reply_response = random.randrange(0, 4)
    print(begin_response, reply_response)
    reply = beginning[begin_response] + f"{item.name} " + replies[reply_response]
    return reply


id = [66]


def study_reminder(api, since_id, account):
    item = api.get_user(account)
    logger.info("Reminding people to Study")
    print("YO", id)
    new_since_id = since_id
    for status in tweepy.Cursor(api.user_timeline, id=account, since_id=since_id, tweet_mode='extended').items(10):
        print(type(status.id))
        if status.id in id:
            continue
        else:
            print("YOOOOOOOO")
            print(id)
            id.append(status.id)
            reply = "@" + account + " " + generate_reply(item)
            print(status.id, status.full_text)
            api.update_status(reply, in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        accounts = ["jakeparatha1", "NagshaktiNagesh", "BedardiBaalma"]
        for x in accounts:
            print("YOOO")
            since_id = study_reminder(api, since_id, x)
            logger.info("Waiting....")
            time.sleep(30*10)


if __name__ == "__main__":
    main()
