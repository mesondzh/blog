#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime

import csdn
from twitter import APIKey, ITwitter

from utils import config_all
from twitter import backup_tweets
from typecho import get_article

twitter_config = config_all["twitter"]


if __name__ == "__main__":
    # twitter
    now = datetime.now()
    my_tweets_file = "post/twitter/{}-{}-{}-my-tweets.md".format(now.year, now.month, now.day)
    backup_tweets(twitter_config, my_tweets_file)

    # # csdn
    # csdn.spider("ds19991999", "utils/cookie.txt", "post/csdn")
    #
    # # typoche
    # get_article("post/typecho")
