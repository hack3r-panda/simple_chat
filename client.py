import sys
import socket
import time

s = socket.socket()
host = input("enter the hostname: ")
port = 3333
uname = input("enter the username: " )

print("wating for the server for response....")
time.sleep(1)

s.connect((host, port))
print("connection found!")

#reciving username
rname = s.recv(1024)
rname = rname.decode()
print(rname + " has joined!" )

#sending user name
sname = s.send(uname.encode())

while True:
	try:
		print(rname + " is typing...")
		rmessage = s.recv(1024)
		rmessage = rmessage.decode()
		print(rname + " : " + rmessage)
		message = input("message: ")
		smessage = s.send(message.encode())
		print("Sent")
	except EOFError as e:
		print(e )
		exit()
	