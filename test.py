# -*- coding: utf-8 -*-

from  demdownload import download
from querydata import querydata
import requests


url1="http://www.gscloud.cn/search/query"
allID=querydata(url1)
for each in allID:
    ID=each["dataid"]
    url2="http://www.gscloud.cn/sources/download/310/"+ID+"/bj"
    print(url2)
    headers={
        "Host":"www.gscloud.cn",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":"http://www.gscloud.cn/search",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":'csrftoken=c81wO0xlKTM0yTpVZwIYPXel70jS3P0s; _next_="/"; gscloud_session=m5tlo0huscpwmpvqur8ywgprdp1a5f3y; upost="up:wk7L99zmPdhQxetsoZNzU8T6-nEkzDPW7s4lTJ0xs7_KxAIu3Hv_wXn_4CpZdvigzAM"; utoken="ut:8W4fcqfpNel4avzWP0ZJ0k1r"'
        }
    # filename = url.split('/')[-1].strip()
    # filename = "respose.log"
    # r=requests.get(url=url2, headers=headers, stream=True)
    # print(r.text)

















