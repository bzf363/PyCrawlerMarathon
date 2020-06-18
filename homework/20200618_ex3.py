# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import xmltodict #import 套件xmltodict為推薦套件

with open ('/Users/chenshihti/Desktop/PyCrawlerMarathon/homework/example_ex3/64_Week24_CH.xml') as fd:
    
    doc = dict(xmltodict.parse(fd.read())) #將資料讀出
    
    #打開文字檔，一層一層的找你要的資料，找到含內容text的那層為止
    #往下拉到最後比較容易看架構
    docdata = doc['cwbopendata']['dataset']['locations']['location']
    print (len(docdata))
    
    for i in docdata:
        #請問高雄市有多少地區有溫度資料
        print (i['locationName']) #查找docdata中list內的key就能把資料讀出來
    
     
    #location內的資料型態為list不能往下剝 
    #取list的時候用index號碼代替，有orderdict時可以再改取key值
    
    #請取出每一個地區所記錄的第一個時間點跟溫度    
    doctemp1=[] #時間
    doctemp2=[] #溫度
    for i in range (0, len(docdata), 1):    
        doctemp1.append(doc['cwbopendata']['dataset']['locations']['location'][i]['weatherElement'][0]['time'][0]['startTime'])
        doctemp2.append(doc['cwbopendata']['dataset']['locations']['location'][i]['weatherElement'][0]['time'][0]['elementValue']['value'])
    
    #請取出第一個地區所記錄的每一個時間點跟溫度
    
    doctemp1area=doc['cwbopendata']['dataset']['locations']['location'][0]['weatherElement'][0]['time']
    
    doctemp1area1=[] #時間
    doctemp1area2=[] #溫度
    for i in range(0, len(doctemp1area), 1):
        
        doctemp1area1.append(doctemp1area[i]['startTime'])
        doctemp1area2.append(doctemp1area[i]['elementValue']['value'])
