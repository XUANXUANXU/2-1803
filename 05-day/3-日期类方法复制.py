class DateTest():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def outDate(self):#实例方法
		print("%s年%s月%s日"%(self.year,self.month,self.day))
	@classmethod
	def handleDate(cls,date):
		a,b,c = date.split("-")
		d = cls(a,b,c)
		return d		
str = '2019-03-23'
DateTest.hadlerDate(str).outDate()
