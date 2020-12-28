#!/bin/python3
import sys
import socket 
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPV4
else :
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
print("." * 50)
print("Scanning target " + target)
print("Time started: "+str(datetime.now()))
print("." * 50)

try:
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port)) # returns an error indicator
		if result == 0:
			print(f"port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
except socket.gaierror: # cant connect to host 
	print('Host name could not be resolved')
	sys.exit()
except socket.error: # if nothing can be connected
	print('Could\'t connect to server')
	sys.exit()