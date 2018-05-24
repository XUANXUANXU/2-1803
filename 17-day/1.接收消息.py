from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',7788))
s.sendto("小可爱".encode("gb2312"),("192.168.1.104",6666))

content,info = s.recvfrom(1024)
print('%s-----%s'%(content.decode('gb2312'),info[0]))

s.close()