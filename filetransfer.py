#!/usr/bin/python3

import logging
import paramiko


logger = logging.getLogger(__name__)



def file_recv(ip, username, password, src_file, dst_file, port):
    logger.info('Start file recive function.')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=username,
                    password=password, timeout=5, port=port)
    except Exception as connection_error:
        logger.error('Connection failed %s' % connection_error)
        return False
    sftp = ssh.open_sftp()
    try:
        sftp.get(src_file, dst_file)
    except Exception as error:
        logger.error('Error in recive file %s' % error)
        return False
    sftp.close()
