from multiprocessing import Process
import time
import os

def test(name):
	for i in range(5):
		time.sleep(2)
		print("你相信星座么%s"%name)
p = Process(target=test,args=('宝贝儿',) )
p.start()

p.join()
print("不信")
