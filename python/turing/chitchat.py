#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json

key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def chitchat(chats):
    config =  {"key":key,"info":chats}
    postdata = json.dumps(config)

    r = requests.post("http://www.tuling123.com/openapi/api",data=postdata)
    data = r.text
    updata = json.loads(data)
    return updata['text']
