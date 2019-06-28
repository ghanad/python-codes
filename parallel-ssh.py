#! /usr/bin/env python3

from __future__ import print_function
from pssh.clients import ParallelSSHClient

username = 'root'
pass_word = 'a'
port = 22
log_path = '/var/log/pnd-ipos.log'

hosts = ['10.1.1.1', '10.1.1.2']
client = ParallelSSHClient(hosts, port=port , user=username, password=pass_word)

output = client.run_command('echo -ne "$(cat /etc/hostname) | " ;echo -ne "$(date | cut -d " " -f 2,3,4) | " ;  iostat -x 2 5 | grep sda | tail -n 1')


f = open(log_path, 'a')

for host, host_output in output.items():
	if host_output.exit_code == 0:
		for line in host_output.stdout:
			print(line)
			f.write(line + "\n")
	else:
		f.write("Exit Code is not 0.")	
	
f.write('-----------------------\n')
f.close()
