file_name = input("请输入文件的名字")
old_file = open(file_name,"r")

position = file_name.rfind(".")
file_name[0:position]
file_name[position:]
new_file_name = file_name[0:position]+"备份"+file_name[position:]
new_file = open(new_file_name,"w")
while True:
	content = old_file.read(1024)
	if len(content) == 0:
		break
	new_file.write(content)


old_file.close()
new_file.close()
