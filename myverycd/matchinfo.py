# -*- coding: utf-8 -*-
# Name:        利用正则式匹找出需要的元素
# Purpose:
# Author:      libin
# Created:     2014/2/12
#-----------------------------------------------------------------------------------------------------------------------

import re
import sqlite3

from ispider import download
conn = sqlite3.connect('myverycd.bd')
conn.text_factory = str

def infomatch(strdate,db=conn):
    #date = re.compile(r"<h1>(.*?)vistor",re.DOTALL).findall(strdate)[0]
    prog_title = re.compile(r'<h1>(.*?)<',re.DOTALL) #匹配出title
    title = prog_title.findall(strdate)
    prog_
    return ''.join(title)


def main():
    date = download(1, 'entries')
    t = infomatch(date)
    print t


if __name__ == '__main__':
    main()