def w2(p):
	def w1(fun):
		def inner(*args,**kwargs):
			if p == '哈哈':
				print('验证')
			elif p == '呵呵':
				print('验证')
			ret = fun(*args,**kwargs)
			return ret
		return inner
	return w1

@w2('哈哈')
def test(a,b):
	print('a = %d b = %d'%(a,b))
	return '1张晨波是个傻逼'

@w2('呵呵')
def test1():
	print('2张晨波是个傻逼')

@w2('讷讷')
def test2(a,b):
	print('3张晨波是个傻逼')

@w2('恩恩')
def test3():
	return '4张晨波是个傻逼'

test1()
test2(1,2)
print(test3())
print(test(1,2))
