class Animal():

	def __init__(self):
		self.__name = "晨波"
	def getname(self):
		return self.__name
	def eat(self):
		print('吃吃吃')
	def sleep(self):
		print("睡睡睡")

	def __money(self):
		print('私有财产')
	def askmoney(self):
		self.__money()

class Dog(Animal):
	pass
class Cat(Animal):
	pass
taidi = Dog()
taidi.eat()
taidi.sleep()
taidi.askmoney()
print(taidi.getname())

mao = Cat()
mao.eat()
mao.sleep()
mao.askmoney()
print(mao.getname())
