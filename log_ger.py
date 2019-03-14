#! /usr/bin/env python3

# version 1.0
# 2/13/2019
# first edition

##########
##copy to liberary directory
##cp log_ger.py /usr/lib/python3/dist-packages/

##########
##   to use as module:
#import log_ger
#my_logger = log_ger.get_logger(__name__ + "Logger")
#my_logger.debug("---------a debug message")

import logging
import sys
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"

def get_console_handler():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

def get_file_handler():
        file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)
        return file_handler

def get_logger(logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)                  #Log level
        logger.addHandler(get_console_handler())        #to print logs on console
        #logger.addHandler(get_file_handler())          #to write logs on file
        logger.propagate = False
        return logger


#my_logger = get_logger(__name__ + "Logger")
#my_logger.debug("---------a debug message")



