#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2016年4月14日 下午9:36:35

@author: zhuGe
'''
import json
'''
    创建sql模块
'''
def build_sql(json_str):
    obj = json.loads(json_str)
    sql = "insert into douban("
    sql_values = "values("
    
    for k, v in obj.items():
        if isinstance(v, bool):
            v = str(v)
        #_sql关键字替换
        if k=='desc':
            k = k+'s'
        
        sql += k+','
        sql_values += "'"+v+"',"
    return (sql[:-1]+")"+sql_values[:-1]+")")


'''
    示例
print(build_sql('{"loc_id":"108296","name":"无聊的头","created":"2005-03-03 02:26:33","is_banned":false,"is_suicide":false,"loc_name":"上海","avatar":"http://img3.douban.com\/icon\/u1000005-11.jpg","signature":"","uid":"the.56s.head","alt":"http:\/\/www.douban.com\/people\/the.56s.head\/","desc":"","type":"user","id":"1000005","large_avatar":"http://img3.douban.com\/icon\/up1000005-11.jpg"}'))
'''