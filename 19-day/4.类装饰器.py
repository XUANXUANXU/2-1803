def w(cls):
	def w1(*args,**kwargs):
		return cls(100)
	return w1
@w
class Dog():
	def __init__(self,x):
		self.x = x
dog = Dog(5)
print(dog.x)