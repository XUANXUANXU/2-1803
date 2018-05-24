from threading import Thread
import time
import threading
num = 100

def work1():
    global g_num
    for i in range(100):
        num += 1

    print(num)


def work2():
    global g_num
    for i in range(100):
    	num += 1
    print("%st    %d"%num)


print("---线程创建之前g_num is %d---"%num)

t1 = Thread(target=work1)
t1.start()

time.sleep(1)

t2 = Thread(target=work2)
t2.start()
