from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.sendto("你爹".encode("gb2312"),("192.168.1.104",6666))
s.close()