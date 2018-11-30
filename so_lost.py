#!/usr/bin/env/python3

import socket
 
host = '52.61.142.146'
port = 31802
 
# Create socket and connect
s = socket.socket()
s.connect((host, port))
 
# Receives up to 1024 bytes
data = s.recv(1024)
s.listen()
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
