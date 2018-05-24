def w1(fun):
	def inner():
		print("哈哈哈哈")
		fun()
	return inner


def test():
	print("哈哈哈哈哈")

test = w1(test)
test()




