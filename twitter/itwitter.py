#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
twitter developer app: https://developer.twitter.com/en/portal/projects-and-apps
function: backup my own tweets to local file and empty my tweets on twitter
date: 2021-02-21 01:39
"""

import twitter
import tweepy
from tweepy.api import API
from tweepy.auth import AppAuthHandler
from tweepy.binder import pagination

class APIKey(object):
    def __init__(self, consumer_key, consumer_secret, bearer_token, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.bearer_token = bearer_token
        self.access_token = access_token
        self.access_token_secret = access_token_secret

class ITwitter(object):
    def __init__(self, key:APIKey, proxy=''):
        self.key = key
        self.proxy = proxy
        self.status_ids = set()
        self._init()

    def _init(self):
        auth = tweepy.OAuthHandler(self.key.consumer_key, self.key.consumer_secret)
        auth.set_access_token(self.key.access_token, self.key.access_token_secret)
        self.api = tweepy.API(
            auth_handler=auth,
            proxy=self.proxy, 
            wait_on_rate_limit=True, 
            wait_on_rate_limit_notify=True
            )

    def get_tweets(self, local_file):
        page = 1
        with open(local_file, "w", encoding="utf-8") as f:
            while True:
                public_tweets = self.api.user_timeline(page=page)
                for tweet in public_tweets:
                    self.status_ids.add(tweet.id)
                    line = "* {} | {} | {}".format(tweet.created_at, tweet.source, tweet.text)
                    print(line)
                    f.write(line+"\n")
                if len(public_tweets) < 20:
                    break
                else:
                    page += 1
    
    def empty_tweets(self):
        for status_id in self.status_ids:
            if (status_id==1368458750005145600):
                continue
            self.api.destroy_status(status_id)
            print(status_id, 'deleted!')


def backup_tweets(twitter_config, my_tweets_file):
    key = APIKey(
        consumer_key = twitter_config["consumer_key"],
        consumer_secret = twitter_config["consumer_secret"],
        bearer_token = twitter_config["bearer_token"],
        access_token = twitter_config["access_token"],
        access_token_secret = twitter_config["access_token_secret"]
    )
    twitter = ITwitter(key,"http://127.0.0.1:7890")
    twitter.get_tweets(my_tweets_file)
    twitter.empty_tweets()

    