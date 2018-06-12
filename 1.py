import random
class tool():
	def __init__(self):
		self.list = [1]

	def add(self):
		for i in range(10):
			while True:
				count = random.randint(1,100)
				if count not in self.list:
					self.list.append(count)
					break
		print(self.list)

	def function1(self):
		self.list.sort()
		print(self.list)
		d = random.randint(0,len(self.list)-1)
		print("随机数为%d,索引为%d"%(self.list[d],d))
		print(self.list)

	def function2(self):
		for i in range(len(self.list)):
			for j in range(len(self.list)):
				if self.list[i] < self.list[j]:
					self.list[i],self.list[j] = self.list[j],self.list[i]
		h = random.randint(0,len(self.list)-1)
		print("随机数为%d,索引为%d"%(self.list[h],h))
		print(self.list)		
			
if __name__=="__main__":
	c = tool()
	c.add()
	c.function1()
	c.function2()
