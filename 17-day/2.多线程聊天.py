from socket import *
from threading import Thread

s = None
port = 0
ip = ''
def  send():
	while True:
		content = input("请输入内容")
		s.sendto(content.encode('gb2312'),(ip,port))

def recv():
	while True:
		msg = s.recvfrom(1024)
		print("%s-----%s"%(msg[0].decode('gb2312'),msg[1][0]))

def main():
	global s
	global port
	global ip
	ip = input("请输入ip地址")
	port = int(input("请输入端口"))
	s = socket(AF_INET, SOCK_DGRAM)
	s.bind(('',8888))
	t = Thread(target=send)
	t.start()
	t1 = Thread(target=recv)
	t1.start()
	t.join()
	t1.join()
if __name__ == '__main__':
	main()

