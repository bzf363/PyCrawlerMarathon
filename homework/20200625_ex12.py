#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:11:18 2020

@author: chenshihti
"""


import requests
from bs4 import BeautifulSoup
#from lxml import etree
#from PIL import Image
import os

h={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

r= requests.get ('https://www.ettoday.net/news/news-list.htm',headers=h)

soup = BeautifulSoup(r.text,'lxml')

#print (soup)

soup1=soup.select('.part_list_2') # select只能選一個 全部內容 不能印text

#取出今天所有的發文
       
#for i in soup1: 
     #print(i.text)
 
#如果想要依照類別分類，怎麼儲存會比較好

res={}


#print (soup.find(class_="part_list_2").find_all('h3')) #find能選很多個，或是用find+find_all搭配


for d in soup.find(class_="part_list_2").find_all('h3'):
    date = d.find(class_="date").text #將日期存成單一str
    
    title = d.find('a').text #  同title = d.find_all('a')[-1].text

    #title = d.find_all('a')[-1].text #all裡面的倒數第一個
    
    tag = d.find(class_='tag').text
    #tag = d.select('.tag')[0].text #tag為新聞分類
    
    res.setdefault(tag, []) #setdefault設默認值 key=tag valuse=list
    res[tag].append({'title': title,'date': date}) #list內設dict
    
#print(res)

#哪一個類別的文章最多

data = []
    
for i in res:
    d = {}
    d['tag'] = i
    d['count'] = len(res[i])
    #print (len(res[i]))
    data.append(d)

#for d in sorted(data, key=lambda d: d['count'])[::-1]:
    
              #(list, key=lambda 元素: 元素[字段索引]) 元素可以自行定義
    #print(d)
    

print (sorted(data, key=lambda x: x['count']))

    
"""

soup2=soup.select('em',recursive=False)

a=[]

for i in soup2:
    print (i.getText())
    a.append(i.text)
    
print ('財經',a.count('財經'))
print ('體育',a.count('體育')) #哪一個類別的文章最多
print ('政治',a.count('政治'))
print ('影劇',a.count('影劇'))
print ('生活',a.count('生活'))
print ('寵物動物',a.count('寵物動物'))
print ('社會',a.count('社會'))
print ('地方',a.count('地方'))
print ('時尚',a.count('時尚'))
print ('3C家電',a.count('3C家電'))
print ('消費',a.count('消費'))
print ('大陸',a.count('大陸'))
print ('國際',a.count('國際'))
print ('房產雲',a.count('房產雲'))
print ('ET車雲',a.count('ET車雲'))

"""



