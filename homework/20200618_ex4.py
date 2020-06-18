#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:49:41 2020

@author: chenshihti
"""


import requests #引入api函數
import json
#想要爬資料的 標網址
r= requests.get('https://www.dcard.tw/_api/forums/job/posts?popular=true')

response1=r.text
response2=json.loads(r.text)

for i in response2:
    print (i['excerpt'])