#!/usr/bin/python3
import os
import time
import log_ger
import fnmatch


path1 = "C:\\12"
sleep_time = 1
file_filter = '*Data*'

logger = log_ger.get_logger(console=True, file=False)


def human_size(bytes, units=[' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']):
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


def max_num(list_name):
    max = 0
    for i in list_name:
        try:
            f_num = int(i.split("-")[1])
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
            logger.info("file:%s\tsize:%s" % (i, human_size(dir1[i])))
            file_sum = dir1[i] + file_sum

        logger.info('---------')