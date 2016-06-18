#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2016年4月16日 下午4:58:14

@author: zhuGe
'''
#打开数据库连接
from cn.sunxyz.db.ConnectorUtil import open_cursor, close, cursor_execute
from cn.sunxyz.factory.Build_sql import build_sql
from cn.sunxyz.proxy.Proxy import Url
open_cursor()

#使用代理工具连接
proxy = Url();
#获取json数据1001545 重复
for a in range(1006000,1007379):
    json = proxy.urlopen("http://api.douban.com/v2/user/"+str(a))
    print(json)
    if json!=None:
        sql = build_sql(json)#调用 sql工厂 拼装sql
        print("save",a) #存储数据
        cursor_execute(sql)

#关闭数据库连接
close()
