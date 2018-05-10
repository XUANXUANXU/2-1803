#单列模式
class Dog(object):
	__instance = None #私有类属性
	__init_flag = False
	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance


	def __init__(self,name):
		if Dog.__init_flag == False:
			self.name = name
			Dog.__init_flag = True
dog1 = Dog('xiaoming')
dog2 = Dog('xiaohong')
dog3 = Dog('xiaogang')
print(id(dog1))
print(id(dog2))
print(id(dog3))
print(dog1.name)
print(dog2.name)
print(dog3.name)





















