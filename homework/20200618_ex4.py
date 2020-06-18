#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:49:41 2020

@author: chenshihti
"""


import requests #引入api函數
import json
#想要爬資料的 標網址
r= requests.get('http://odata.wra.gov.tw/v4/RealtimeWaterLevel')

response1=r.text
response2=json.loads(r.text)
