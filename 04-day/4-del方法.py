class dog():
	def __init__(self):
		pass
	def __str__(self):
		return 

	def __del__(self):
		print("del方法被执行了")
taidi = dog()
erha = taidi
del taidi
del erha
print("hahahah")
