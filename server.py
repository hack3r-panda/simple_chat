import sys
import socket
import time

s = socket.socket()
host = socket.gethostname()
print(host)
port = 3333
uname = input("enter the username: " )

s.bind((host, port))
s.listen()

print("wating for connection....")
time.sleep(2)

conn ,addr = s.accept()
print("connection found!")

#sending user name
sname = conn.send(uname.encode())


#reciving username
rname = conn.recv(1024)
rname = rname.decode()

print(rname + " has joined!" )

while True:
	try:
		message = input("message: ")
		smessage = conn.send(message.encode())
		print("Sent")
		print(rname + " is typing..." )
		rmessage = conn.recv(1024)
		rmessage = rmessage.decode()
		print(rname + " : " + rmessage)
	except EOFError as e:
		print(e )
		exit()
	