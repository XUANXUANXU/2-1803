class Dog():
	age = 99
	def __init__(self,name):
		self.name = name
		Dog.age += 2
	def walk(self):
		print("汪汪叫")
	@classmethod
	def lei(cls):
		print('这是类方法')
	@classmethod
	def change(cls):
		cls.age +=1

taidi = Dog('泰迪')
print(taidi.name)
taidi.walk()
taidi.lei()
print(taidi.age)

taidi.change()
print(Dog.age)
print(taidi.age)
