class Dog():
	def __init__(self):
		self.__money = 100
	def setmoney(self,money):
		if money <= 0:
			print('不行!!!')
		else:
			self.__money = money
	def getmoney(self):
		return self.__money
xiaoming = Dog()
xiaoming.setmoney(12)
print(xiaoming.getmoney())
