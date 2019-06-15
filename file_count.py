#!/usr/bin/python3

# version 1.5
# author: Ghanad

import os
from datetime import datetime
import time
import sys
import multiprocessing


src_dir = '/home/ali/test/'

if len(sys.argv) >= 2:
	dir_filter=sys.argv[1]
else:
	dir_filter=''


class counter:
	def __init__(self):
		pass
	
	## get modify time of file		
	def mdate(self, file1):
		self.file1 = file1
		return datetime.fromtimestamp( os.path.getmtime(self.file1)).strftime('%Y-%m-%d')

	## create list of times in a directory 
	def date_list(self, path):
		self.path= path
		date_list1 = []
		for i in os.listdir(self.path):
			date_list1.append( counter.mdate(self, self.path+i) )	
		return list( dict.fromkeys(date_list1) )

	def f_count(self, dpath):
		self.dpath = dpath
		for i in counter.date_list(self, self.dpath):
			ab = len( list( filter( lambda x: counter.mdate(self, self.dpath+x) == i , os.listdir(self.dpath)  )))
			print ('%0-*s\t%s\t%s' % (max_len, self.dpath, i, ab))

if __name__ == '__main__':
	
	dir_list=[]	
	for i in os.listdir(src_dir):
		if os.path.isdir(src_dir+i) and dir_filter in i:
		#if os.path.isdir(src_dir+i):
			dir_list.append(src_dir+i+'/')

	try:
		max_len= len(max(dir_list))
	except:
		pass

	thread_list = list()
	obj_list = []
	
	#create instance for eche directory and append to list
	for i in range(0, len(dir_list)):
		a = counter()
		obj_list.append(a)

	#creata thread and append to list
	for i in range(0, len(dir_list)):
		thr = multiprocessing.Process(target = obj_list[i].f_count , args=(dir_list[i],))
		thread_list.append(thr)


	for i in range(0, len(thread_list)):
		thread_list[i].start()	
