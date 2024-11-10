import json
# full path or absolute path
#file = open("/Users/danielkong/Documents/jason/text.txt", "rb")
#f = open("D:\\myfiles\welcome.txt", "r")

# relative path
# file = open("../jason/text.txt")

# for x in file:
# 	d = json.loads(x)
# 	print(d['name'])

# file2 = open("../jason/text.txt", "w")
# file2.write("{'name': 'daniel', 'age': 12}")
# file2.close()

# file2 = open("../jason/text.txt", "r")
# print(file2.read())

# file3 = open("textabc.txt", "x")

import os

os.mkdir("Documents")

if os.path.exists("Documents"):
	print("Folder Exists")
	os.rmdir("Documents")
	print("Folder Deleted")
else:
	print("error")

#Try Except


# open("text.txt", "x")
# try:
# 	os.remove("text.txt")
# except:
# 	print("Error")
# else:
# 	print("Success")