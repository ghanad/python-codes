#!/usr/bin/python3

#version 1.2
#author: Ghanad

import os
from datetime import datetime
import time
import json
import log_ger
import sys
import shutil


src_path = '/home/ali/test/t3/'
dst_path = '/home/ali/test/dst/'
out_path = '/home/ali/test/dst/'
dst_limit=100
out_limit=100
sleep_time=30

days = ['2019-05-20', '2019-05-19']

logger = log_ger.get_logger(file=False)
logger.info('start script')

## find out date of given file 
def mdate(file2):
	return datetime.fromtimestamp( os.path.getmtime(file2)).strftime('%Y-%m-%d')


## number of files for given date
def count_date(src_path1, date1):
	mc = 0
	for i in os.listdir(src_path):
		if mdate(src_path1+i) ==  date1:
			mc = mc + 1
	return mc


logger.info('source path is:%s' % src_path)
logger.info('destination path is:%s' % dst_path)
list_date = list()

for i in days:
	count1 = count_date(src_path, i)
	list_date.append(count1)
#for i in list_date:
	logger.info('Number of files for date %s in source direcoty is:%s' % (i , count1))
total = 0
for i in days:
	while count_date(src_path , i) > 0:
		logger.info('start while loop')
		file_count_day = count_date(src_path , i)
		logger.info('number of files for day:%s is: %s' % (i, file_count_day))
		for j in sorted(os.listdir(src_path), key=lambda x: mdate(src_path + x) == i , reverse=True):
			dst_len = len(os.listdir(dst_path))
			out_len = len(os.listdir(out_path))
			if dst_len < dst_limit and out_len < out_limit:
				logger.info('_file:%s    date:%s' % (j , mdate(src_path+j)))
				if mdate(src_path+j) == i:
					shutil.move(src_path+j, dst_path)
					logger.info('__move file:%s' % j)
					total = total + 1
				else:
					logger.info('__flie:%s date has different date with %s' % (j, i ))
			else:
				file_count_day = count_date(src_path , i)
				logger.info('dst file no:%s. out file no: %s. files for %s is:%s. total copied file is:%d' % (dst_len, out_len, i, file_count_day,total))
				time.sleep(sleep1_time)
		logger.info('end of loop for files in directory')
