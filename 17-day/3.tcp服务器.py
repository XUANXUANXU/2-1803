from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('',3334))
s.listen(5)
newSocket, info = s.accept()
while True:
	content = newSocket.recv(1024)
	print(content.decode('gb2312'))
	#print(content)

