class OP(object):
	def __init__(self,num1 = 0,num2 = 0 ):
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
class Factory(object):
	def create_op(self,type):
		if type == "+":
			return Jia()
		elif type == "-":
			return Jian()
		elif type == "*":
			return Cheng()
		elif type == "/":
			return Chu()
xiao = Factory()
jia = xiao.create_op("+")
jia.num1 = 1
jia.num2 = 2
print(jia.getResult())		
