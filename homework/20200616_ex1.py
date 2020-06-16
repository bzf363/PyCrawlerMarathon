#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:04:23 2020

@author: chenshihti
"""

from urllib.request import urlretrieve as ul
import os

#建立Data資料夾

fpath= "/Users/chenshihti/Desktop/Data"
if os.path.exists(fpath):
    print ("不用建立")
else:
    os.mkdir(fpath)

#下載指定檔案到Data資料夾，存成檔名Homework.txt
    
ul ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./Data/Homework.txt")

#檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

if os.path.isfile("/Users/chenshihti/Desktop/Data/Homework.txt"):
    print ("file exists")
else:
    print ('filde doesn\' t exist')

#將「Hello World」字串覆寫到 Homework.txt 檔案

with open ("/Users/chenshihti/Desktop/Data/Homework.txt",'w') as fn:
    fn.write("Hello World")

#檢查 Homework.txt 檔案字數是否符合 Hello World 字數
    
with open ("/Users/chenshihti/Desktop/Data/Homework.txt",'r')as fn2:
    countfn2=fn2.read()

#用rstrip()將文字間的空格切除，len()計算檔案的長度
    
finalcountal=countfn2.rstrip()
orignal= "Hello World"
orignal2=orignal.rstrip()

if len(finalcountal) == len(orignal2):
    print ("檔案字數符合 Hello World 字數")
else:
    print ("檔案字數不符合 Hello World 字數")       