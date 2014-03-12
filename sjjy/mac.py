#coding=utf-8
# Name:        
# Purpose:
# Author:      libin
# Created:     
#-----------------------------------------------------------------------------------------------------------------------
import uuid
import socket

class macname:
    "获取客户端mac地址与客户端的用户名"

    # myname = ""
    # mac = ""
    def get_mac_address(self):
        node = uuid.getnode()
        self.mac = uuid.UUID(int = node).hex[-12:]
        #获取本机电脑名
        self.myname = socket.getfqdn(socket.gethostname(  ))
        self.mac = ":".join([self.mac[e:e+2] for e in range(0,11,2)])

# #获取本机ip
# myaddr = socket.gethostbyname(myname)
# print myname
# print myaddr

def main():
    mymac=macname()
    mymac.get_mac_address()
    print(mymac.mac,mymac.myname)

if __name__ == '__main__':
    main()