#coding=utf-8
# Name:        
# Purpose:
# Author:      libin
# Created:     
#-----------------------------------------------------------------------------------------------------------------------

import pymongo
import datetime
import  globalpara


class DB_mongo():
    "实现数据在mongoDB中存储的类"

    def __init__(self,list):
        con = pymongo.Connection('localhost', 27017)
        self.db = con.sjjy_test
        self.list =list
        # self.mytable = self.db.table_working  #不要使用table_working 除非是正式程序
        # self.mytable2 = self.db.table_err #不要使用table_err 除非是正式程序
        # self.mytable3 = self.db.table_neterr  #不要使用table_neterr 除非是正式程序
        self.mytable_data = self.db.table_working_test0 #测试用
        self.mytable_err = self.db.table_err_test0 #测试用
        self.mytable_neterr = self.db.table_neterr_test0 #测试用

    def write(self):
        # print(self.db)
        # print(self.mytable)
        if len(self.list) == 7:
            post1= {"urlID":self.list[0],"sex":self.list[1],"age":self.list[2],"xinzuo":self.list[3],"location":self.list[4]
                     ,"height":self.list[5],"degree":self.list[6],"datetime":datetime.datetime.now(),
                    "macNO":globalpara.Global_mymacNo,"PCname":globalpara.Global_PCName}
            self.mytable_data.insert(post1)
        elif len(self.list) == 2:
            post_err = {"urlID":self.list[0],"err_reasons":self.list[1],"datetime":datetime.datetime.now(),
                        "macNO":globalpara.Global_mymacNo,"PCname":globalpara.Global_PCName}
            self.mytable_err.insert(post_err)
        else:
            print("err!!")

    def write_neterr(self,url):
        post_neterr = {"url":url,"try_times":"5","datetime":datetime.datetime.now(),"macNO":"test01"}
        self.mytable_neterr.insert(post_neterr)

def main():
    DB_mongo([1110987575, u'\u7537', 28, u'\u767d\u7f8a\u5ea7', u'\u5b89\u5fbd\u5408\u80a5', 178, u'\u5927\u4e13']).write()
    # DB_mongo([1110987575,"other reasons"]).write()

if __name__ == '__main__':
    main()