#!/usr/bin/python3
import os
from datetime import datetime
import time
import json

src_path = '/home/ali/test/'



def mdate(file2):
	return int(datetime.fromtimestamp( os.path.getmtime(file2)).strftime('%d'))


dir_list=[]
dir_count={}
for i in os.listdir(src_path):
	if os.path.isdir(src_path + i):
		dir_list.append(src_path+i+'/')
		dir_count[src_path+i+'/']=[]


for i in dir_list:
	for j in os.listdir(i):
		m_day = mdate(i+j)
		if m_day not in (x[0] for x in dir_count[i]):
			temp_list = [m_day,1]
			dir_count[i].append(temp_list)
		else:
			for z in range(len(dir_count[i])):
				if m_day in dir_count[i][z]:
					dir_count[i][z][1] = dir_count[i][z][1] + 1 


for i in dir_count:
	print ('%s  %s' % (i, dir_count[i]))
