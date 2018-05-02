class Home():
	def __init__(self,area,address,price,hometype):
		self.area = area
		self.address = address
		self.price = price
		self.hometype = hometype
		self.jiaju = []

	def __str__(self):
		msg = "房子的面积是%d平方\n房子的地址是%s\n房子的价格是%d万\n房子的类型是%s"%(self.area,self.address,self.price,self.hometype)
		return msg

	def addbed(self,bed):
		if self.area >= bed.getarea():
			self.jiaju.append(bed)
			self.area-=bed.getarea()
			print('添加成功')
			print(self.area)
		else:
			print("失败")


class Bed():
	def __init__(self,area,color,price,pinpai):
		self.area = area
		self.color = color
		self.price = price
		self.pinpai = pinpai
	def __str__(self):
		msg = "床的大小是%d平方\n床的颜色是%s\n床的价格是%d元\n床的品牌是%s"%(self.area,self.color,self.price,self.pinpai)
		return msg

	def getarea(self):
		return self.area


class Light():
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return "我叫%s灯"%self.name



myhome = Home(500,"天安门广场",9999,"别墅")
print(myhome)
mybed = Bed(100,"姨妈色",666,"Gucci")
print(mybed)
benladeng = Light("本拉登")
print(benladeng)

myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
myhome.addbed(mybed)
