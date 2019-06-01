#! /usr/bin/env python3
#version 1.3

import logging
import sys
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"


def get_console_handler():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler


def get_file_handler(log_file):
        file_handler = TimedRotatingFileHandler(log_file, when='midnight')
        file_handler.setFormatter(FORMATTER)
        return file_handler


def get_logger(level = 'INFO' ,logger_name=sys.argv[0][2:-3], console=True, file=False, log_file=sys.argv[0][2:-3]+'_report.txt'):
        logger = logging.getLogger(logger_name)

        #set log level 
        logger.setLevel(level.upper())

        # to print logs on console
        if console == True:
                logger.addHandler(get_console_handler())
        
        # to write logs on file
        if file == True:
                logger.addHandler(get_file_handler(log_file))

        logger.propagate = False
        return logger


##########
# to use as module:
#import log_ger
#my_logger = log_ger.get_logger(__name__, console=True, file=False)
#my_logger.debug("---------a debug message")
