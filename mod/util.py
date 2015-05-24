# -*- coding: utf-8 -*-
import json

CONFIG = "./config.json"


def get_config(FILE_PATH):
    j = open(FILE_PATH, 'r')
    return json.load(j)
