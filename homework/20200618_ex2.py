#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:10:47 2020

@author: chenshihti
"""


#File I/O

osfile= open ('/Users/chenshihti/Desktop/example＿ex2.csv','r') #將檔案打開，無法看具體內容
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
    for i in range (0,len(listreport),1):
        print(listreport[i][5])
    
    # 2. 將班次一的每一個時間用一個變數保存
    
    datastorage2=[]
    for i in range (0,len(listreport),1):
        datastorage2.append(listreport[i][5])
    # 3. 將所有班次和其每一個時間用一個變數保存
        
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]
    data8=[]
    data9=[]
    data10=[]
    data11=[]
    for i in range (0,len(listreport),1):
        data2.append(listreport[i][6])
        data3.append(listreport[i][7])
        data4.append(listreport[i][8])
        data5.append(listreport[i][9])
        data6.append(listreport[i][10])
        data7.append(listreport[i][11])
        data8.append(listreport[i][12])
        data9.append(listreport[i][13])
        data10.append(listreport[i][14])
        data11.append(listreport[i][15])



        
    
        
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