'''
Created on Oct 19, 2014

@author: crysisx
'''
#!/usr/bin/python
import socket
get=0
address = ('', 515)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(address)

while True:
    data, addr = s.recvfrom(2048)
    get=get+1
    if not data:
        print "client has exist"
        break
    print "received:", data, "from", addr
    print "get",get

s.close()
