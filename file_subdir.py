import os

#src_dir = '/home/ali/test'
src_dir='D:\\test\\'


def Cfile(root_dir, filter=''):
	total=0
	for dirName, subdirList, fileList in os.walk(root_dir):
		for fname in fileList:
			if fname.startswith(filter):
				total = total + 1
	return total

print(Cfile(src_dir))