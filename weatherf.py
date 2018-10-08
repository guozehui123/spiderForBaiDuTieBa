# -*- coding:utf-8 -*-

import requests
from lxml import etree
import re
import time
print("现在时间为:" + time.ctime())
print("-"*50)

url = 'http://www.weather.com.cn/weather1d/101280601.shtml'
headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
html = requests.get(url, headers=headers).text
#print html
#with open("weather.txt","wb") as f:
#    f.write(html)
selector = etree.HTML(html)
#获取数据
#获取天气情况
tianqi= selector.xpath('//div[@class="t"]//li/p[@class="wea"]')
print("今天深圳的天气为:")
print(tianqi[0].text)
#今天温度
print("-"*50)
wendu= selector.xpath('//div[@class="con today clearfix"]//ul[@class="clearfix"]//p[@class="tem"]/span')
print("今天的最高温和最低温度为:")
for link in range(len(wendu)):
    print(wendu[link].text + "摄氏度")


print("-"*50)
print("今天的日出和日落时间为:")
#日出时间
richu= selector.xpath('//div[@class="t"]//p[@class="sun sunUp"]/span')
for link in range(len(richu)):
    print(richu[link].text)
#日落时间
riluo = selector.xpath('//div[@class="t"]//p[@class="sun sunDown"]/span')
for link in range(len(riluo)):
    print(riluo[link].text)
#异常天气
print("-"*50)
yichang= selector.xpath('//div[@class="con today clearfix"]//div[@class="t"]//div[@class="zs w"]/span')
print("今天可能出现的异常天气:")
for link in range(len(yichang)):
    print(yichang[link].text)
if yichang == []:
    print("无异常天气")
