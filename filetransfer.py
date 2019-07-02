#!/usr/bin/python3

import logging
import paramiko

username = 'root'
password = 'a'


logger = logging.getLogger(__name__)


def file_recv(ip , username, password , src_file, dst_file, port):
	logger.info('{{file_recv}} Start.')

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(ip, username=username, password=password, timeout=5 , port=port)
	except:
		logger.error('{{file_recv}} Connection failed')
		return False
	sftp = ssh.open_sftp()
	try:
		sftp.get(src_file, dst_file)
	except Exception as error:
		logger.error('{{file_recv}} %s' % error)
		return False
	sftp.close()
