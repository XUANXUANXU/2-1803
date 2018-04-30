class Pig():
	def eat(self):
		print('我喜欢吃柠檬味的薯片耶')
	def sleep(self):
		print('如果一天睡24小时我会很开心')
	def introduce(self):
		print('我的名字是%s\n我今年%s\n我的皮肤是%s\n'%(self.name,self.age,self.color))

peiqi=Pig()
peiqi.name = '小猪佩奇'
peiqi.age = '3岁了啦'
peiqi.color = '粉红色哦'
peiqi.eat()
peiqi.sleep()
peiqi.introduce()


fhzxm=Pig()
fhzxm.name = '粉红猪小妹'
fhzxm.age = '5岁了哦'
fhzxm.color = '粉红色的呢'
fhzxm.eat()
fhzxm.sleep()
fhzxm.introduce()
