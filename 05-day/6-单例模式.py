class Dog(object):

	__instance = None #私有类属性

	def __new__(cls):

		if cls.__instance == None:

			cls.__instance = object.__new__(cls)

			return cls.__instance

		else:

			return cls.__instance





	def __init__(self,name):

		self.name =  name

	

dog1 = Dog("xiaoming")

dog2 = Dog("xiaohong")

dog3 = Dog("xiaogang")

dog4 = Dog("xiaowang")

dog5 = Dog("xiaolan")



print(id(dog1))

print(id(dog2))

print(id(dog3))

print(id(dog4))

print(id(dog5))

print(id(dog2))
