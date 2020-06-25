#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:10:51 2020

@author: chenshihti
"""


import requests
from bs4 import BeautifulSoup
from lxml import etree
#from PIL import Image
import os


#output_dir = 'download3'
#os.makedirs(output_dir)

h={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
r= requests.get("https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html", cookies={'over18': '1'}, headers=h)

soup= BeautifulSoup(r.text,'lxml') #以lxml做為解析器（必寫）

xml=etree.HTML(r.text)

img_id=xml.xpath('//blockquote[@class="imgur-embed-pub"]/@data-id')


#下載圖片
for i in range(len(img_id)):
    img_url = ('https://imgur.com/%s.jpg' %(img_id[i]))
    picture=requests.get(img_url)    
    print ("下載圖片",img_id[i])
    
#存圖片    
    fname ='photo'+img_id[i]
    with open (fname, 'wb') as f:
        f.write(picture.content)