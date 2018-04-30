class Gilr():
	def __init__(self,name,age,color):
		self.name = name
		self.age = age
		self.color = color
		self.game = ['妲己','貂蝉','庄周','虞姬']

	def car(self,car):
		print("开的%s"%car)
	def han(self):
		print("焊车门")
	def show(self):
		print('名字是%s年龄是%d颜色是%s'%(self.name,self.age,self.color))
	def showgame(self):
		for i in self.game:
			print(i)
xueman = Gilr('娄司机',17,'黑色')
xueman.car('奇瑞')
xueman.han()
xueman.show()
xueman.showgame()
