# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = "http://news.baidu.com"
data = requests.get(url)
s = BeautifulSoup(data.text.encode(data.encoding), "lxml")
title = s.select("#pane-news > div > ul > li.hdline0")
print(title)


