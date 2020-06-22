#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:50:24 2020

@author: chenshihti
"""


import requests
from bs4 import BeautifulSoup
#from lxml import etree
from PIL import Image
import os
h={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
r= requests.get("https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html", cookies={'over18': '1'}, headers=h)


output_dir = 'download2'
os.makedirs(output_dir)



#xml=etree.HTML(r.text)

#img_id=xml.xpath('//blockquote[@class="imgur-embed-pub"]/@data-id')
#img_link=xml.xpath('//*[(@id = "imgur-embed-iframe-pub-IjiETcs")]')

soup= BeautifulSoup(r.text,'lxml') #以lxml做為解析器（必寫）
print (soup.prettify())

#找連結下的主id再找圖片連結通常是a

image_tags = soup.find(id='main-content').findChildren('a', recursive=False)

for img in image_tags:
    # 取得所有圖片在第三方服務的 id
    img_id = img['href'].split('/')[-1] #以/分隔 數據在最後面所以用-1
    # 組合圖片而非網站的網址
    img_url = 'https://i.imgur.com/{}.jpg'.format(img_id)
    # 對圖片送出請求
    with requests.get(img_url, stream=True) as r:
        r.raise_for_status()
        # 檢查圖片副檔名
        img = Image.open(r.raw)
        img_savename = '{outdir}/{img_id}.{img_ext}'.format(
            outdir=output_dir, img_id=img_id, img_ext=img.format.lower())
        img.save(img_savename)
        print('Save image {}'.format(img_savename))