def m1(fn):
	def wa():
		print(123)
		fn()
	return wa
def m2(fn):
	def wa():
		print(456)
		fn()
	return wa

def m():
	print(789)

m = m2(m)
m = m1(m)
m()
