#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, yaml

def get_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config.yaml")
    with open(config_path, "r", encoding="utf-8") as config_file:
        configdata = yaml.safe_load(config_file.read())
    return configdata
config_all = get_config()

