class Dog(object):
	def __init__(self):
		self.__name = "xueman"
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,name):
		self.__name = name

dog = Dog()
dog.name = 'xuan'
print(dog.name)
