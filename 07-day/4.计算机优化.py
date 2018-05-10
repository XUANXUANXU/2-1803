class Jia():
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def jia(self):
		return self.num1+self.num2

class Jian():
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def jian(self):
		return self.num1-self.num2

class Cheng():
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def cheng(self):
		return self.num1*self.num2

class Chu():
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def chu(self):
		if self.num2 != 0:
			return self.num1/self.num2
j = Jia(1,5)
print(j.jia())
