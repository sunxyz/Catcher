#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2016年4月14日 下午10:35:37

@author: zhuGe
'''
from urllib import request

#获取连接中的数据
def urlopen(url_path):
    try:
        #使用代理
        proxy_support = request.ProxyHandler({'sock5': 'localhost:1080'})
        opener = request.build_opener(proxy_support)
        request.install_opener(opener)
        req = request.Request(url_path)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')        #打开链接
        with request.urlopen(req) as f:
            if f.status==200:
                data = f.read()
                return data.decode('utf-8')
    #出现异常不处理
    except Exception :
        pass

