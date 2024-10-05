#!/usr/bin/env python3
'''Check if certificate need to be created or renew'''

# General imports
import os

# Constants
# nginx conf.d path
NGINX_CONF = os.path.join(os.sep, 'etc', 'nginx', 'conf.d')

def main():
	'''main function'''
	# iterate over files in that directory
	for filename in os.listdir(NGINX_CONF):
		file = os.path.join(NGINX_CONF, filename)
		# checking if it is a file
		if os.path.isfile(file):
			domain = filename.replace('.conf', '')
			cmnd = f'newcert.sh {domain}'
			print(f'INFO: Calling {cmd}.')
			os.system(cmd)
	os.system('nginx -t && nginx -s reload')

# starting the check for renew
if __name__ == "__main__":
	main()
