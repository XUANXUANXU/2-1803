def fib():
	n = 0
	a,b = 0,1
	while n<8:
		a,b = b,a+b
		#print(b)
		print("dada")
		yield b
		print("haha")
		n+=1

b = fib()
print(b)
		
