#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:47:18 2020

@author: chenshihti
"""


import requests
from bs4 import BeautifulSoup
from lxml import etree
#from PIL import Image
import os

h={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

r= requests.get ('http://jimmypm.ehosting.com.tw/new001151.htm',headers=h)

soup = BeautifulSoup(r.text,'lxml')

#整理資料，找出圖片路徑 並收集

p_collect=[]

for i in soup.select('img'):
     p_collect.append(i['src'])

#製作圖片的url並下載圖片
     
for i in range (len(p_collect)):
    p_url=("http://jimmypm.ehosting.com.tw/%s" %(p_collect[i]))
    picture=requests.get(p_url)
    
#存圖片    
    fname ='photo'+p_collect[i]
    with open (fname, 'wb') as f:
        f.write(picture.content)

