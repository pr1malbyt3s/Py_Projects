#!/usr/bin/env/python

import socket

#Assign host and port address
host = '52.61.142.146'
port = 31802
 
#Create socket and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#Loop through data received to send proper response. 
while True:
  data = s.recv(1024).decode('utf-8')
  print(data)
  if '\nup' in data:
    s.send('^\n'.encode('utf-8'))  
  elif '\ndown' in data:
    s.send('V\n'.encode('utf-8'))
  elif '\nleft' in data:
    s.send('<\n'.encode('utf-8'))
  elif '\nright' in data:
    s.send('>\n'.encode('utf-8'))
  else:
    break

#Close connection
s.close()
