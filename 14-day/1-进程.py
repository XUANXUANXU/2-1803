import os
pid = os.fork()
if pid == 0:
	print('我是子进程%d pid=%d ppid=%d'%(pid,os.getpid(),os.getppid()))
else:
	print('我是父进程%d pid=%d ppid=%d'%(pid,os.getpid(),os.getppid()))

