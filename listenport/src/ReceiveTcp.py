'''
Created on Oct 19, 2014

@author: crysisx
'''
#!/usr/bin/python
#-*- coding: utf-8 -*-
from socket import *
from time import ctime
HOST=''
PORT=515
BUFSIZ=2048
ADDR=(HOST,PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
get=0
while True:
    print 'waiting for connection...'
    tcpCliSock,addr=tcpSerSock.accept()
    print '...connected from:',addr

    while True:
        data=tcpCliSock.recv(BUFSIZ)
        get = get+1
        if not data:
            break
        print 'get',get
        print "received:", data,"address",addr
    tcpSerSock.close()
    tcpCliSock.close()