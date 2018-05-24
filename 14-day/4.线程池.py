
from multiprocessing import Pool
import time
import os

def work(a):
	for i in range(3):
		time.sleep(1)
		print('我是%d'%a)



p = Pool(9)
for i in range(10):
	print(i)
	p.apply(work,(i,))
p.close()
p.join()
