class Digua():
	def __init__(self):
		self.cooklever = 0
		self.cookstr = "生的"
		self.lientes = []
	def __str__(self):
		return self.cookstr+str(self.lientes)
	def cook(self,time):
		self.cooklever += time
		if 0 < self.cooklever < 3:
			self.cookstr = "半生不熟"
		elif 3 <= self.cooklever < 5:
			self.cookstr = "熟啦"
		elif self.cooklever >= 5:
			self.cookstr = "糊啦"
	def add(self,zuoliao):
		self.lientes.append(zuoliao)

mydigua = Digua()
mydigua.cook(1)
mydigua.add("放点盐")
print(mydigua)
mydigua.add("上点芥末")
mydigua.cook(1)
mydigua.add("放点味精")
print(mydigua)
mydigua.add("放点鸡精")
mydigua.cook(1)
mydigua.add("放点醋")
print(mydigua)
mydigua.add("放点粗")
mydigua.cook(1)
mydigua.add("放点酱油")
print(mydigua)
mydigua.add("放点香菜")
mydigua.cook(1)
mydigua.add("放点小葱")
print(mydigua)
mydigua.add("放点火腿肠")
mydigua.cook(1)
mydigua.add("放点萝卜丁")
print(mydigua)
