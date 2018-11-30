#!/usr/bin/env/python

import socket
import sys
  
host = '52.61.142.146'
port = 31802
 
# Create socket and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#data = s.recv(4096)
while True:
    data = s.recv(1024)
    print(data)
    sdata = data.decode('utf-8')
    if "/nup" in sdata:
      s.send(b"^")
    elif "/ndown" in sdata:
      s.send(b"V")
    elif "/nleft" in sdata:
      s.send(b"<")
    elif "/nright" in sdata:
      s.send(b">")
# Close connection
s.close()
