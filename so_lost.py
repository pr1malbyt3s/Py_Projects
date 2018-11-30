#!/usr/bin/env/python

import socket
import sys
  
host = '52.61.142.146'
port = 31802
 
# Create socket and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#while True:
data = s.recv(1024).decode('utf-8')
print(data)
if "\nup" in data:
  s.send("^".encode('utf-8'))
elif "\ndown" in data:
  s.send("V".encode('utf-8'))
elif "\nleft" in data:
  s.send("<".encode('utf-8'))
elif "\nright" in data:
  s.send(">".encode('utf-8'))
# Close connection
s.close()
