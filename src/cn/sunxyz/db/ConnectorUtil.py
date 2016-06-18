#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2016年4月14日 下午8:04:38
数据库连接工具
@author: zhuGe
'''
import mysql.connector

#print(mysql)
'''
    建立数据库连接
'''
def open_cursor():
    global conn, cursor
    conn = mysql.connector.Connect(
                        host='127.0.0.1',
                        port = 3306,
                        user = 'root',
                        password = 'root',
                        database = 'sprider'
                        ) 
    cursor = conn.cursor()
 
'''
    执行数据操作
'''   
def cursor_execute(sql):
    try:
        cursor.execute(sql)
        cursor.rowcount
        conn.commit()
    except:
        pass
    finally:
        conn.rollback()

#print(conn)
#print(cursor)

'''
    关闭数据库
'''
def close():
    cursor.close()
    conn.close()