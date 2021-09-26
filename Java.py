







import os
dir1 = "/sdcard/MyTemp/"
if (os.path.isdir(dir1)):
	os.chdir(dir1)
	list1 = os.listdir()
	for v in list1:
		if v.endswith('.java'):
			with open(v)as r:
				c = r.read()
			os.chdir("/sdcard/Java")
			s = v.split('.java')[0]
			with open(v, "w") as wr:
				wr.write(c)
			os.chdir("/sdcard/MyTemp/")
			os.remove(v)
		#else:
		#)	print("No Java File Exist")
else:
		os.mkdir("/sdcard/MyTemp")
		print("ReRun The Program Please")
		
		
		
#def python1():
#	dir1 = "/storage/emulated/0/MyTemp/"
#	if (os.path.isdir(dir1)):
#		os.chdir(dir1)
#		list1 = os.listdir()
#		print(list1)
#	else:
#		os.mkdir("/sdcard/MyTemp")
#		print("ReRun The Program Please")
#		
#if __name__ == '__main__':
#	input1 = input("java or python: ")
#	if (input == "java"or input == "Java" or input == "JAVA"):
#		Java()
#	elif(input == "python"or input == "Python" or input == "PYTHON"):
#		python1()