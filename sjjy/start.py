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
import threading
import datetime

class worker():
    "负责在客户端生成一个任务"

    def down(self):
        #i =0
        #threads = []
        #urlpool = globalpara.Global_urlpool
        #global i
        #start_time = time.clock()
        # for k in range(0,1):
        # Cth = spider(1100070)
        # Cth.start()
        Cth = spider(globalpara.Global_urlpool)
        #threads[i] = Cth
        #i+=1
        Cth.start()
        globalpara.Global_urlpool+=1
        return Cth
        #time.sleep(0.05)

class monitor():
    "一种失败的多线程，就好像没有多线程一样，难道是GIL的关系？"

    def __init__(self,slavenum,totalnum):
        self.slavenum = slavenum
        self.totalnum = totalnum

    def manager(self):
        print("start:",datetime.datetime.now())
        rcount = 0
        while True:
            rcount+=1
            if ((globalpara.Global_urlpool - 1100000) >= self.totalnum):
                break
            else:
                threads = []

                for j in range(0,self.slavenum):
                    w =spider(globalpara.Global_urlpool)
                    t = threading.Thread(target=w.run())
                    threads.append(t)

                for i in range(0,self.slavenum):
                    threads[i].start()
                    globalpara.Global_urlpool+=1

                for k in range(0,self.slavenum):
                    threads[k].join()
                    print (threads[k])
                print ("round:",rcount)
        print("done!",datetime.datetime.now())



def main():
    "改4个参数，globalpara.Global_urlpool-1600000 >= totalnum: "

    slavenum = 100
    totalnum = 100000
    mymac = macname()
    mymac.get_mac_address()
    globalpara.Global_mymacNo = mymac.mac
    globalpara.Global_PCName = mymac.myname
    i =0
# ##test 2
#     m = monitor(10,100)
#     m.manager()
#test 1
    print("start at:",str(datetime.datetime.now()))
    while True:
        i+=1
        if globalpara.Global_urlpool-2400000 >= totalnum:
            break
        else:
            threads = []
            for j in range(0,slavenum):
                w=worker().down()
                threads.append(w)
                time.sleep(0.0005)
                print(globalpara.Global_urlpool)
                print(threads)
        threadlen = len(threads)
        # for k in range(0,threadlen):
        #     threads[k].join()
        while True:
            alive = 0
            for k in range(0,threadlen):
                alive |= threads[k].isAlive()
            if not alive:
                break
            else:
                continue
        print('round:',i)
    # for j in range(0,1000):
    #     worker().down()
    #     time.sleep(0.05)
    #     print(globalpara.Global_urlpool)
    #         # len1 =  len(threads)
    #         # for i in range(0,len1):
    #         #     threads[i].join()
    # threads = []
    # for j in range(0,slavenum):
    #     Cth = spider(globalpara.Global_urlpool)
    #     threads.append(Cth)
    #     Cth.start()
    #     globalpara.Global_urlpool+=1
    #     time.sleep(0.05)
    #     print(globalpara.Global_urlpool)

    #len1 =  len(threads)
    # for i in range(0,len1):
    #     threads[i].join()
    print("done!")
    print("end at:",str(datetime.datetime.now()))


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