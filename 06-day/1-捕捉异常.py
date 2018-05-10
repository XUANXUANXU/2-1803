try:
	10/0
	print(轩轩好美)
	print("轩轩美炸了")
	open("xxx.tet")
except (NameError,ZeroDivisionError):
	print("出错了")
except Exception as result:
	print("捕捉所有异常")
	print(result)
finally:
	print("错不错都走这里")
print("我美了美了我醉了醉了")
