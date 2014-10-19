'''
Created on Oct 19, 2014

@author: crysisx
'''
#!/usr/bin/python
#-*- coding: utf-8 -*-
import socket
port=515
host='107.189.158.4'
i=0
end =raw_input("how many logs?")
end = int(end)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(0,end):
    s.sendto(b'11.11.1.1 - - [01/Mar/2013:12:23:53 +0800] "GET /v1/api HTTP/1.1" api.xx.com 200 4003 "https://api.xx.com/v1/api" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)" "-" 10.1.1.1:80 200 - "text/html;charset=UTF-8" 0.023 > 0.023',(host,port))
    print 'send',i+1