#!/usr/bin/env/python

import socket
import sys
  
host = '52.61.142.146'
port = 31802
 
# Create socket and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

buffer = ''
while True:
  data = s.recv(4096)
  if data:
    print data
    if "/nup" in data.decode('utf-8'):
      s.send(b"^")
    elif "/ndown" in data.decode('utf-8'):
      s.send(b"V")
    elif "/nleft" in data.decode('utf-8'):
      s.send(b"<")
    elif "/nright" in data.decode('utf-8'):
      s.send(b">")
  else:
    break
# Close connection
s.close()
