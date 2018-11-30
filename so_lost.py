import socket
 
host = 'challenge.acictf.com'
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
