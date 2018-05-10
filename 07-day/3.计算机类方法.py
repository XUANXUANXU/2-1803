class Op():
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def jia(self):
		return self.num1+self.num2
	def jian(self):
		return self.num1 - self.num2
	def cheng(self):
		return self.num1 * self.num2
	def chu(self):
		if self.num2 != 0:
			return self.num1/self.num2
op = Op(1,2)
print( op.jia())
