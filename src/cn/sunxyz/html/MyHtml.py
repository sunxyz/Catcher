#coding:utf-8
'''
Created on 2016年4月16日

@author: zhuGe
'''
from html.parser import HTMLParser
import re



class MyHtml(HTMLParser):
    '''
    classdocs
    '''
    def __init__(self, *, convert_charrefs=True):
        HTMLParser.__init__(self)
        self._lists = []
    
    a_t=False  
    def handle_starttag(self, tag, attrs):  
        #print("开始一个标签:",tag)  
        if str(tag).startswith("td"):   
            self.a_t=True  
  
    def handle_endtag(self, tag):  
        if tag == "td":  
            self.a_t=False  
            #print("结束一个标签:",tag)  
  
    def handle_data(self, data):  
        if self.a_t is True: 
            k = re.match("\d.*\d$", data) 
            if k:
                num = k.group(0)
                #print(num)
                self._lists.append(num)
            #print("得到的数据:",data) 
    @property
    def lists(self):
        return self._lists 
    @lists.setter
    def lists(self, lists):
        self._lists= lists
