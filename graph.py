#!/usr/bin/python3
import os
import time
import log_ger
import fnmatch


path1 = "C:\\12"
sleep_time = 1
file_filter = '*Data*'

logger = log_ger.get_logger(console=True, file=False)

def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes>>10, units[1:])

def max_num(list_name):
	max = 0
	for i in list_name:
		try:
			f_num =  int(i.split("-")[1])
		except:
			pass
		if f_num > max:
			max = f_num
	return max

while True:
	dir1 = {}
	for i in fnmatch.filter(os.listdir(path1), file_filter):
		j = os.path.join(path1, i)
		size1 = os.path.getsize(j)
		dir1.update({i: size1})

	time.sleep(sleep_time)

	dir2 = {}
	for i in fnmatch.filter(os.listdir(path1), file_filter):
		j = os.path.join(path1, i)
		size2 = os.path.getsize(j)
		dir2.update({i: size2})

	
	kdir1 = dir1.keys()
	kdir2 = dir2.keys()	

	k_diff = list(set(kdir1) - set(kdir2))


	file_sum = 0
	if k_diff:
		for i in k_diff:
			logger.info("file:%s\tsize:%s" %(i , human_size(dir1[i])))
			file_sum = dir1[i] + file_sum

		## find near files
		for j in kdir2:
			for z in range(max_num(k_diff) - 3 , max_num(k_diff) + 3):
				if str(z) in j:
					if  int(dir2[j]) < file_sum*1.1 or int(dir2[j]*0.9) < file_sum :
						logger.info("Near file:%s\tdiff:%f"  %(j , dir2[j]/file_sum))
						#logger.info("Near file:%s\tsize:%s\t\tfiles removed size:%s"  %(j , human_size(dir2[j]), human_size(file_sum)))

		logger.info('---------')
