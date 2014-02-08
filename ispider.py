#coding=utf-8
# Name:        
# Purpose:
# Author:      libin
# Created:      2014/02/05
# 这是一个爬虫程序，实现对网站的下载  改动了文件
#屌炸天！！！！！！！！！！！
#-----------------------------------------------------------------------------------------------------------------------

#这是一个下载程序，输入id,suburl:子域名（entries，topics等）
def download(id, suburl):
    import re
    import time
    import urllib

    url_root = 'http://www.verycd.com/'  #根域名
    url = url_root + suburl + '/' + str(id)  #全域名
    for i in range(10):  #尝试10次下载
        down_ok = False
        try:
            file_get = urllib.urlopen(url).read()
            down_ok = True
            break  #下载成功跳出循环
        except:
            #1次不成功休息1m继续
            time.sleep(1)
            continue

    if not down_ok:  #10次没成功将这一情况记录到数据库中
        #report_download_fail(url,发生时间)
        print('下载失败')
    else:
        print('下载成功')


def main():
    download(1, 'entries')


if __name__ == '__main__':
    main()