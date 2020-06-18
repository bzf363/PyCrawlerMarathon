#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:10:47 2020

@author: chenshihti
"""


#File I/O

osfile= open ('/Users/chenshihti/Desktop/example.csv','r') #將檔案打開，無法看具體內容
content=osfile.read() # .read() 才能看到檔案實際資料
#print(content)
osfile.close()

with open ('/Users/chenshihti/Desktop/example.csv','r') as osfile2:
    content2=osfile2.read() # .read() 才能看到檔案實際資料
    #print(content2)
    
#CSV Reader

import csv

with open ('/Users/chenshihti/Desktop/example.csv','r') as osfile3:
    csvReader=csv.reader(osfile3) #將檔案打開，無法看具體內容
    
    # method 1
    
    listreport =list(csvReader) #轉list才可以看資料
    #for i in range (1,len(listreport),1):
    # 1. 取出班次一的每一個時間
    print(listreport[1][5:15:1])
    # 2. 將班次一的每一個時間用一個變數保存
    datastorage1=listreport[1][5:15:1]
    datastorage2=[]
    # 3. 將所有班次和其每一個時間用一個變數保存
    for i in range (1,len(listreport),1):
        datastorage2.append(listreport[i][5:15:1])
        
    
        
    """
    #method 2 需要把line33#才可以作用
    b=[]
    for row in csvReader:
        b.append(row)
    """    
"""
# pandas

import pandas as pd

pdread= pd.read_csv('/Users/chenshihti/Desktop/example.csv')
"""