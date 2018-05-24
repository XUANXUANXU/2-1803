def fib():
	n = 0
	a,b = 0,1
	while n<8:
		a,b = b,a+b
		#print(b)
		yield b
		n+=1

b = fib()
print(b)
print(next(b))		
print(next(b))		
print(next(b))		
print(next(b))		
print(next(b))		
print(next(b))		
