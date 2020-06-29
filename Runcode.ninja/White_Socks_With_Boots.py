#!/usr/bin/env python3

# This is a simple script to demonstrate connecting to a raw socket and parsing received data.

import sys
import socket

# Get host and port from command line.
HOST = sys.argv[1]
PORT = int(sys.argv[2])
#IP = socket.gethostbyname(HOST)

# Create and connect to socket. Print received data.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(s.recv(1024).decode('utf-8').strip())
s.close()
