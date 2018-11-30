#!/usr/bin/env/python

import socket
import sys
  
host = '52.61.142.146'
port = 31802
 
# Create socket and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

try:
 while 1:
  data = s.recv(1024)
  print data
  stringdata = data.decode('utf-8')
  if "/nup" in stringdata:
   s.send(b"^")
  elif "/ndown" in stringdata:
   s.send(b"V")
  elif "/nleft" in stringdata:
   s.send(b"<")
  elif "/nright" in stringdata:
   s.send(b">")
 
# Close connection
s.close()
