#!/usr/bin/python3
import os
import time


path1 = "C:\\12"

while True:
	dir1 = {}
	for i in os.listdir(path1):
		j = os.path.join(path1, i)
		size1 = os.path.getsize(j)
		dir1.update({i: size1})

	time.sleep(2)

	dir2 = {}
	for i in os.listdir(path1):
		j = os.path.join(path1, i)
		size2 = os.path.getsize(j)
		dir2.update({i: size2})

	# change file size	
	for key1 , value1 in dir1.items():
		for key2 , value2 in dir2.items():
			if key1 == key2:
				if value1 != value2:
					print('file:%s\told:%s\tnew:%s' %( key1 , value1 , value2 ) )


	n1 = list(dir1.keys())
	n2 = list(dir2.keys())
	if len(n1) != len(n2):
		# Remove file 
		print(list(set(n1) - set(n2)))

	if len(n2) != len(n1):
		# add
		print(list(set(n2) - set(n1)))
