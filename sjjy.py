#coding=utf-8
# Name:        
# Purpose:
# Author:      libin
# Created:     
#-----------------------------------------------------------------------------------------------------------------------

import urllib2
import time
import StringIO
import gzip
import threading
from infomatch import infoMatcher
from DB import DB_mongo


class spider(threading.Thread):
    "爬虫类，并负责下载爬到的网页"
    
    url_web = "http://www.jiayuan.com/"
    url_id = 0

    def __init__(self,intid):
        threading.Thread.__init__(self)
        self.lock = threading.Lock()
        self.url_id = intid
        #self.lock = threading.Lock()

    def report(self,url):
        #报告错误
        DB_mongo(["neterr"]).write_neterr(url)

    def run(self):
        start_time = time.clock()
        #global i
        self.url_id+=1
        url = self.url_web+str(self.url_id)

        for count in range(0,5):
            down_ok = 0
            req_header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                        'Accept-Encoding':'gzip'}
            request = urllib2.Request(url,None,req_header)
            try:
                web_get = urllib2.urlopen(request,None,timeout=10)
                down_ok = 1
                break
            except:
                time.sleep(0.001)
                continue
        if down_ok !=1:
            self.report(url)
        else:
            predata = web_get.read() #下载gzip格式的网页
            pdata = StringIO.StringIO(predata)#下面6行是实现解压缩
            gzipper = gzip.GzipFile(fileobj = pdata)
            try:
                data = gzipper.read()
            except(IOError):
                print 'unused gzip'
                data = predata#当有的服务器不支持gzip格式，那么下载的就是网页本身
            #self.lock.acquire()
            list = infoMatcher(data,self.url_id).domatch()
            DB_mongo(list).write()
            #self.lock.release()
            # filter1 = re.compile("查看详细信息(.*?)婚",re.DOTALL)
            # content = filter1.findall(data)
            # data1 = ''.join(content)
            # path="D:\\test1\\"+str(i)+'.txt'
            # i+=1
            # open(path,'w').write(data1)
            # #print(urlpool)
            # self.lock.release()
            # end_time = time.clock()
            # print(i,'---',end_time-start_time)
            #return data1
            #self.lock.release()

    def download1(self):
        #这个方法效率不如download()
        self.url_id+=1
        url = self.url_web+str(self.url_id)
        for k in range(0,10):
            for count in range(0,5):
                down_ok = 0
                req_header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                                    'Accept':'text/html;q=0.9,*/*;q=0.8','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Connection':'close'}
                request = urllib2.Request(url,None,req_header)
                try:
                    web_get = urllib2.urlopen(request,None,timeout=10)
                    down_ok = 1
                    break
                except:
                    time.sleep(0.001)
                    continue
            if down_ok !=1:
                self.report()
            else:
                data3 = web_get.read()
                return data3


    def read(self,web_in):
        read_size = 1024*8
        read_once = ''
        web_str = ''

        while True:
            read_once = web_in.read(read_size)
            if read_once == '':
                break
            web_str +=read_once
        return web_str