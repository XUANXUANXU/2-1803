class Dog(object):
	def __init__(self):
		print("init方法")
	def __str__(self):
		print("str方法")
		return '返回值'
	def __del__(self):
		print("del方法")
	def __new__(cls):
		print("new方法")
		return object().__new__(cls)

dog = Dog()
print(id(dog))
