#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:49:41 2020

@author: chenshihti
"""


import requests #引入api函數
import json #所讀取的資料可以被分類
import numpy as np #計算平均值
#想要爬資料的 標網址
r= requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=true')


response=json.loads(r.text)

#1. 這個 API 一次會回傳幾筆資料？
print(len(response))
print()
#1. 每一筆資料包含哪些欄位？
print(response[0].keys())
print()

#2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
#respone為list 所以可以for i in list
for i in response:
    print(i['title'],i['createdAt'],i['commentCount'],i['likeCount'])
    print()
    
#3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
    
total=len(response)
commentCount=[]
likeCount=[]
for i in range (0, total, 1):
    commentCount.append(response[i]['commentCount'])
    likeCount.append(response[i]['likeCount'])
    
print("commentCount_average",np.mean(commentCount))
print("likeCount_average",np.mean(likeCount))


