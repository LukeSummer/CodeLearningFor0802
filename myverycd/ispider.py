#coding=utf-8
# Name:        
# Purpose:
# Author:      libin
# Created:      2014/02/05
# 这是一个爬虫程序，实现对网站的下载  改动了文件
#-----------------------------------------------------------------------------------------------------------------------

import time
import urllib

#这是一个下载程序，输入id,suburl:子域名（entries，topics等） 输出：网页的源代码，str形式
def download(id, suburl):
    url_root = 'http://www.verycd.com/'  #根域名
    url = url_root + suburl + '/' + str(id)  #全域名
    for i in range(10):  #尝试10次下载
        down_ok = False
        try:
            file_get = urllib.urlopen(url) #打开源代码
            down_ok = True
            break  #下载成功跳出循环
        except:
            #1次不成功休息1m继续
            time.sleep(1)
            continue

    if not down_ok:  #10次没成功将这一情况记录到数据库中
        #report_download_fail(url,发生时间)
        print('下载失败')
        return ''

    read_size = 1024*8 #设置读取的长度为1024*8
    read_num = 0      #读取的次数
    strdate = ''      #返回的str

    while True:
        read_date = '' #每次读到的1024*8大小的str
        read_date = file_get.read(read_size)
        if read_date == '':
            break
        strdate += read_date
        read_num +=1
    return strdate



def main():
    date = download(1, 'entries')
    open('web','w').write(date)


if __name__ == '__main__':
    main()