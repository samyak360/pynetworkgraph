#!/usr/bin/env python2

import  socket
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.10.218"
port=7890

while  1 :
#  sending  data to  target machine 
	msg=raw_input("enter your message :   ")
        s.sendto(msg,(ip,port))
