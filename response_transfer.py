# -*- coding: utf-8 -*-


class getvales():
    def getdict(dict1, values):
        global values1
        global va  # 定义全局变量
        values1 = values
        for k, v in dict1.items():  # 把字典的key和values变成数组
            if k == values:
                va = v

            elif list is type(v):  # 判断类型是不是list
                getvales.getlsit(v)

            elif type(v) is dict:
                getvales.getdict(v, values1)

            else:
                print(str(k) + ":----" + str(v))

        return va

    def getlist(list1):
        for i in list1:
            if list is type(i):
                getvales.getlsit(i)

            elif dict is type(i):
                getvales.getdict(i, values1)
            else:
                print(list1)

if __name__ == "__main__":
    getvales()