#coding=utf-8
# Name:        
# Purpose:
# Author:      libin
# Created:     
#-----------------------------------------------------------------------------------------------------------------------
from sjjy import spider
import globalpara
from mac import macname
import time


class worker():
    "负责在客户端生成一个任务"

    def down(self):
        #urlpool = globalpara.Global_urlpool
        #global i
        #start_time = time.clock()
        # for k in range(0,1):
        Cth = spider(globalpara.Global_urlpool)
        Cth.start()
        globalpara.Global_urlpool+=1
        #time.sleep(0.05)


def main():
    mymac = macname()
    mymac.get_mac_address()
    globalpara.Global_mymacNo = mymac.mac
    globalpara.Global_PCName = mymac.myname

    for j in range(0,10):
        worker().down()
        time.sleep(0.01)
        print(globalpara.Global_urlpool)
    #urlpool = 1100000
    #start_time = time.clock()
    # for k in range(0,10):
    #     worker().start()
    # start_time = time.clock()
    # t1 = spider(1100000)
    # for i in range(0,10):
    #     str1 = t1.download()
    #     path="D:\\test\\"+str(i)+'.txt'
    #     open(path,'w').write(str1)
    #end_time = time.clock()
    #print ('f-',end_time-start_time)

if __name__ == '__main__':
    main()