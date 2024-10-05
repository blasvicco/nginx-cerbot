#!/usr/bin/env python3
'''Create a new certificate if does detect new domain file added to the nginx conf.d folder'''

# General imports
import os
import signal
import subprocess

# Lib imports
import inotify_simple

# Constants
# nginx conf.d path
NGINX_CONF = os.path.join(os.sep, 'etc', 'nginx', 'conf.d')

# Global variable to control the monitoring loop
RUNNING = True

def monitoring(path):
	'''folder monitoring'''
	print(f'INFO: Initializing folder monitoring for {path}.')
	# Create an inotify instance
	inotify = inotify_simple.INotify()
	# Add a watch on the directory for file creation events
	watch_flags = inotify_simple.flags.CREATE
	watch_descriptor = inotify.add_watch(path, watch_flags)
	try:
		while RUNNING:
			# Wait for an event (timeout of 1 second to allow loop to exit quickly)
      events = inotify.read(timeout=1000)
			# Process the events
			for event in events:
				# event.name contains the name of the file that triggered the event
				if event.mask & inotify_simple.flags.CREATE:
					print(f'INFO: New domain configuration found: {event.name}')
					domain = event.name.replace('.conf', '')
					print(f'INFO: Trigger certbot for domain {domain}.')
					subprocess.Popen(['newcert.sh', domain])
	except KeyboardInterrupt:
		print('INFO: Stopping folder monitoring.')
		inotify.rm_watch(watch_descriptor)

def signal_handler(sig, frame):
	'''Signal handler to stop the loop on system shutdown or interrupt'''
	global RUNNING
	print(f'Received signal {sig}. Shutting down gracefully.')
	RUNNING = False

# starting the monitoring
if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)   # Handle Ctrl+C
	signal.signal(signal.SIGTERM, signal_handler)  # Handle system shutdown
	monitoring(NGINX_CONF)

