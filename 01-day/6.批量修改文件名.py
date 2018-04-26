import os
dir_name = input("请输入要修改的文件夹名")
f = os.listdir(dir_name)
os.chdir(dir_name)
for i in f:
	os.rename(i,"精品"+i)




"""
import os
dir_name = input("请输入要修改的文件夹名")
f = os.listdir(dir_name)
os.chdir(dir_name)
for i in f:
	old_dir_name = dir_name +'/'+i 
	new_dir_name = dir_name +'/'+'精品'+i 
	os.rename(old_dir_name,new_dir_name)
"""
