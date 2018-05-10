class OP(object):
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def getResult(self):
		pass
class Jia(OP):
	def getResult(self):
		return self.num1+self.num2	
class Jian(OP):
	def getResult(self):
		return self.num1-self.num2	
class Cheng(OP):
	def getResult(self):
		return self.num1*self.num2
class Chu(OP):
	def getResult(self):
		if self.num2 != 0:
			return self.num1/self.num2
j = Jia(1,5)
print(j.getResult())
