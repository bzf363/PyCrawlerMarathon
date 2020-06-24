#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:26:59 2020

@author: chenshihti
"""


import re

test_string = "Google IP address is 216.58.200.227"

regex=r'(25[0-5]|2[0-4][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9])'

#nb=25[0-5]|2[0-4][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9]

pattern = re.compile(regex)

print(pattern.findall(test_string))

html_a_tag = "<a href=https://movies.yahoo.com.tw/movietime_result.html/id=9467> 時刻表 </a>"

regex1=r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[-a-z0-9_:@&?=+,.!\/~*\'%$]*'

pattern1 = re.compile(regex1)

print (pattern1.findall(html_a_tag))


