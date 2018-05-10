class msg():
	def __sendmsg(self,money):
		money -= 1
		print('发送短信')
	def publicmsg(self,money):
		if money <= 0:
			print('发送失败')
		else:
			self.__sendmsg(money)

msg = msg()
msg.publicmsg(100)
