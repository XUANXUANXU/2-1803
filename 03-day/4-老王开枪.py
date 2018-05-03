#人类
class Ren():
	def __init__(self,name):
		self.name = name
		self.gun = None#默认没有枪
		self.hp = 100 #默认有100滴血

	def zhuangzidan(self,danjia,bullet):#装子弹
		danjia.addbullet(bullet)

	def zhuangdanjia(self,gun,danjia):#装弹夹
		gun.adddanjia(danjia)

	def takegun(self,gun):#老王拿枪
		self.gun = gun

	def opengun(self,diren):#老王开枪
		#拿到一发子弹
		if diren.hp > 0:
			zidan = self.gun.popgunbullet()#告诉我枪给了我一发子弹
			if zidan:
				zidan.kill(diren)#子弹杀人
			else:
				print("没子弹了")
#枪类
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None

	#装弹夹
	def adddanjia(self,danjia):
		self.danjia = danjia
		#print(id(self.danjia))

	def popgunbullet(self):
		return self.danjia.popbullet()
#子弹夹类
class Danjia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	def addbullet(self,bullet):
		self.bullet_list.append(bullet)#加子弹
		#print(len(self.bullet_list))

	def popbullet(self):
		if self.bullet_list:
			return self.bullet_list.pop()#弹出子弹
		else:
			return None
#子弹类
class Bullet():
	def __init__(self):
		self.weili = 5
	#子弹杀人
	def kill(self,diren):
		diren.hp -= self.weili
		if diren.hp <= 0:
			diren.hp = 0
			print("%s死了啦,剩余血量为%d"%(diren.name,diren.hp))
		else:
			print("%s剩余血量%d"%(diren.name,diren.hp))

laowang = Ren("老王")
ak47 = Gun("ak47")
danjia = Danjia(20)#一个弹夹可以装20颗子弹
for i in range(20):
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)#装子弹
laowang.zhuangdanjia(ak47,danjia)#装弹夹
laosong = Ren("老宋")#创建一个人
laowang.takegun(ak47)#老王拿枪
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
