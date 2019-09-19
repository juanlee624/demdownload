# -*- coding: utf-8 -*-

import requests
import types
import json
from response_transfer import getvales
from collections import Iterable

def querydata(url):
    # url="http://www.gscloud.cn/search/query"
    headers ={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Length": "331",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # "Cookie": "_next_="/"; csrftoken=HjiOXSk51j3kA38fp02PIKm2c9l9JC1L; gscloud_session=hx1sb2r2orebbad9rn9ba95t6dp0tt0e; upost="up:73l_HgiTPodbn1yjkpZXqfLmkNz1fHRHVPOZVhCtdM7Dc36TRvi5tpLZMDiSPSj3zUU"; utoken="ut:1m4GyF7H2E2tcePToY27su9D"",
            # "Cookie": "_next_="/"; csrftoken=ONb1XFqFgrpmxOPj7JxWtvOhtDiJJYyL; gscloud_session=08qruw1zh1woyvus1eh3vkknkklk82zt; upost="up:bk6m47mdWDfSdpvwpgXL3WxEJAKiIYx-b9foURTeejUaHgD1PDfkac6wCWw0_aC39Ts"; utoken="ut:im63lopa8ylXRabfGk6OoKOx"",
            "Host": "www.gscloud.cn",
            "Origin": "http://www.gscloud.cn",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://www.gscloud.cn/search",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
            "X-CSRFToken": "ONb1XFqFgrpmxOPj7JxWtvOhtDiJJYyL",
            "X-Requested-With": "XMLHttpRequest"
    }
    params= {
             "tableInfo":{"offset":0,"pageSize":60,"totalPage":1,"totalSize":20,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[]},
             "productId": 310,
             "datatype":"gdem_utm",
             "data":{"qtype":2,"state":{"name":"prod","code":33}}
                  }
    r=requests.post(url.strip(),data=params,headers=headers) #请求响应结果到r
    r1=r.text #以str方式查看response结果
    # print(isinstance(r1, Iterable))
    # r2=json.loads(r1)#把对象转换成一个dict
    r3=eval(r1)#另一种方式把对象转黄成一个dict
    # print(r1)
    # print("r1的类型：%s"%type(r1))
    # print(r2)
    # print("r2的类型：%s"%type(r2))
    # print(r3)
    # print("r3的类型：%s"%type(r3))

    data1=r3['data'] #把响应结果中data对应的values保存到data1中
    # print(type(data1)) #查看data1的type
    # print(data1) #输出data1
    # for each in data1:
    #     # print(type(each))  # 查看data1这个list中元素的存储类型
    #     # print(each["dataid"])
    #     # print(type(each["dataid"]))#查看所有dataid列表的存储类型，每个id存在一个str里面
    #     ID=each["dataid"]
    return data1


url1="http://www.gscloud.cn/search/query"
querydata(url1)






