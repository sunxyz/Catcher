#coding:utf-8
from urllib import request
import random
from cn.sunxyz.html import MyHtml
class Url(object):
    
    def __init__(self):
        global userAgent, proxyIpList, length
        userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0';
        proxyIpList = []
        self._proxy()
        #计算列表大小
        length = len(proxyIpList)-1
        
        
    #获取代理网页
    def _getpage(self, url_path):
        try:
            req = request.Request(url_path)
            req.add_header('User-Agent', userAgent)
            with request.urlopen(req) as f:
                if f.status==200:
                    data = f.read()
                    return data.decode('utf-8')
        except Exception :
            pass
    
    def urlopen(self,url_path):
        try:
            #使用代理
            # opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
            r = random.randint(0,length)
            self.proxy = proxyIpList[r]
            print(self.proxy)
            self.proxy_support = request.ProxyHandler({'HTTP': self.proxy})
            self.opener = request.build_opener(self.proxy_support)
            request.install_opener(self.opener)
            #添加請求頭
            self.req = request.Request(url_path)
            self.req.add_header('User-Agent', userAgent)
            #获取请求数据
            with request.urlopen(self.req) as f:
                if f.status==200:
                    data = f.read()
                    return data.decode('utf-8')
            
        #出现异常不处理
        except Exception :
            pass

    def _proxy(self):
        #获取代理ip
        data = self._getpage('http://www.xicidaili.com/')
        data = data[data.find('<html>'):]
        #解析数据
        h = MyHtml.MyHtml()
        h.feed(data)
        lists = h.lists
        #计数器
        count = 0;
        ip = ''
        #拼装ip
        for v in lists:
            count +=1
            if count%2==0:
                ip = ip+":"+v
                proxyIpList.append(ip)
            else:
                ip = v
        h.close()
        print(proxyIpList)

#url = Url()
#doc = url.urlopen('http://api.douban.com/v2/user/1001054')
#print(doc)