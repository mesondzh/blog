#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, yaml, datetime
from peewee import *
from playhouse.db_url import connect

from utils import config_all

import warnings
warnings.filterwarnings('ignore')


def db_config():
    db_host = config_all["mysql"]["host"]
    db_port = str(config_all["mysql"]["port"])
    db_name = config_all["mysql"]["database"]
    db_user = config_all["mysql"]["user"]
    db_password = config_all["mysql"]["password"]
    db_url = "mysql://"+db_user+":"+db_password+"@"+db_host+":"+db_port+"/"+db_name
    db = connect(db_url)
    return db


class Content(Model):
    cid = AutoField(primary_key=True)
    title = CharField(null=True)
    created = IntegerField(null=True)
    modified = IntegerField(null=True)
    text = TextField(null=True)
    class Meta:
        database = db_config()
        table_name = config_all["mysql"]["db_table"]


def get_article(folder="post"):
    content_db = Content.select().where(Content.text ** "%<!--markdown-->%").execute()
    if not os.path.exists(folder):
        os.makedirs(folder)
    for content in content_db:
        created = str(datetime.datetime.fromtimestamp(content.created))
        text = content.text
        title = content.title
        file_name = created.split(" ")[0]+"-"+title.replace(" ", "-").replace("/", "-")+".md"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder, file_name)
        content = text.lstrip("<!--markdown-->")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("# {}".format(title) + "\n\n")
            f.write(content)


