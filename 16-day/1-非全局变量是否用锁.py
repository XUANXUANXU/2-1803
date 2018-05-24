from threading import Thread
import time
import threading
def work():
	name = threading.current_thread().name
	print(name)
	num = 1
	if name == "Thread-1":
		num+=1
		print("哒哒哒%d"%num)
		time.sleep(1)
	else:
		num+=10
		print("哈哈哈%d"%num)
'''
def work1():
	name = threading.current_thread().name
	print(name)
	time.sleep(2)
	num = 100
	print("呵呵呵%d"%num)
'''

a = Thread(target=work)
a.start()

a1 = Thread(target=work)
a1.start()
