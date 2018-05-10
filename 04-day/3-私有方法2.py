class money():
	def __init__(self):
		self.money = 1000
	def __dock(self,money):
		self.money-=money
		print('扣了%d,还剩%d'%(money,self.money))
	def publicdock(self,money):
		if money<=0:
			print('扣钱失败')
		else:
			self.__dock(money)


bb = money()
bb.publicdock(100)
