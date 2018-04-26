f = open("xxx珍藏版.txt","r")
content = f.read()
print(content)
f.close()


f = open("xxx珍藏复制版.txt","w")
f.write(content)
f.close()

