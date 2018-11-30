#!/usr/bin/env/python3

import socket
 
host = '52.61.142.146'
port = 31802
 
# Create socket and connect
s = socket.socket()
s.connect((host, port))
 
# Receives up to 1024 bytes
data = s.recv(1024)
print "Received data: " + repr(data)
 
# Send response
s.send("Hello World!\n")
 
# Close connection
s.close()
