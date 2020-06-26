#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:15:30 2020

@author: chenshihti
"""

import requests
from bs4 import BeautifulSoup
#from lxml import etree
#from PIL import Image
import os
from pandas.core.frame import DataFrame

h={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

r= requests.get ('https://www.ptt.cc/bbs/Gossiping/index.html',headers=h,cookies={'over18':'1'})

soup = BeautifulSoup(r.text,'lxml')

soup1=soup.find_all('div',"r-ent") #all articles

nb=0

for i in soup1:  
    if i.find('a'): #含有網址確保找到的是文章
        nb+=1 #total number of articles

#印出最新文章的「作者」「標題」「時間」
        
#找出網址

w_list=[]
        
for i in soup1:
    if i.find('a'):
        w=i.find('a')['href']
        #print (w)
        w_list.append(w)

#網址裝回去重新讀取
        
res=[]       

for i in range(len(w_list)):
    r2=requests.get('https://www.ptt.cc%s' % (w_list[i]),headers=h,cookies={'over18':'1'})
    soup2 = BeautifulSoup(r2.text,'lxml')
    data = soup2.select(".article-meta-value")   #作者#標題#時間 全部裝進去
    
    #內容物裝進list之後再分類
    
    for i in data:
        #print (i.text)
        res.append(i.text)

au=[] #0
ti=[] #2
da=[] #3

for i in range (0, len(res), 4):
    au.append(res[i])
for i in range (2, len(res), 4):
    ti.append(res[i])
for i in range (3, len(res), 4):
    da.append(res[i])    

all_data= {'time':da,'author':au,'title':ti}

data_frame=DataFrame(all_data)

print (data_frame[0].sort_values(by=['time']))
        
#印出第一頁所有文章的「作者」「標題」「時間」
"""
for i in soup1:
    if i.find('a'):
       a= i.find('div','author').text
       h= i.find('a')['href'] #herf非class所以用[]
       t= i.find('a').text
       d= i.find('div','date').text
       print ('作者：', a,"標題：",t,'時間：',d)
"""









