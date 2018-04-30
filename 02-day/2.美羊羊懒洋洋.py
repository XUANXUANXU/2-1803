class Sheep():
	def eat(self):
		print('吃保轩头上的青青草原')
	def sleep(self):
		print('睡保轩头上的青青草原')
	def jieshao(self):
		print("我叫%s我今年%d岁我是%s的"%(self.name,self.age,self.color))



lanyang=Sheep()
lanyang.name = '懒洋洋'
lanyang.age = 1
lanyang.color = '白色'
lanyang.eat()
lanyang.sleep()
lanyang.jieshao()
