# -*- coding: utf-8 -*-

import requests
import types
import json
from response_transfer import getvales


url="http://www.gscloud.cn/search/query"
headers ={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "330",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Cookie": "_next_="/"; csrftoken=HjiOXSk51j3kA38fp02PIKm2c9l9JC1L; gscloud_session=hx1sb2r2orebbad9rn9ba95t6dp0tt0e; upost="up:73l_HgiTPodbn1yjkpZXqfLmkNz1fHRHVPOZVhCtdM7Dc36TRvi5tpLZMDiSPSj3zUU"; utoken="ut:1m4GyF7H2E2tcePToY27su9D"",
        "Host": "www.gscloud.cn",
        "Origin": "http://www.gscloud.cn",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.gscloud.cn/search",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        "X-CSRFToken": "HjiOXSk51j3kA38fp02PIKm2c9l9JC1L",
        "X-Requested-With": "XMLHttpRequest"
}
params= {
         "tableInfo":{"offset":0,"pageSize":10,"totalPage":2,"totalSize":0,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[]},
         "productId":310,
         "datatype":"gdem_utm",
         "data":{"qtype":2,"state":{"name":"prod","code":51}}
              }
r=requests.post(url,data=params,headers=headers) #请求响应结果到r
r1=r.text #以str方式查看response结果
r2=json.loads(r1)#把对象转换成一个dict
r3=eval(r1)#另一种方式把对象转黄成一个dict
print(r1)
print("r1的类型：%s"%type(r1))
print(r2)
print("r2的类型：%s"%type(r2))
print(r3)
print("r3的类型：%s"%type(r3))

data1=r3['data'] #把响应结果中data对应的values保存到data1中
print(type(data1)) #查看data1的type
print(data1) #输出data1
for each in data1:
    # print(type(each))  # 查看data1这个list中元素的存储类型
    # print(each["dataid"])
    # print(type(each["dataid"]))#查看所有dataid列表的存储类型
    ID=each["dataid"]
    print(ID)







