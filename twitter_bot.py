import os

import tweepy


class Twitter:
    def __init__(self):
        consumer_key = os.environ["TW_CONSUMER_KEY"]
        consumer_secret = os.environ["TW_CONSUMER_SECRET"]
        access_token = os.environ["TW_ACCESS_TOKEN"]
        access_token_secret = os.environ["TW_ACCESS_TOKEN_SECRET"]
        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

    def tweet(self, text: str):
        self.client.create_tweet(text=text)
        print("tweet completed.")
