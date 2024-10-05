#!/bin/sh

# Adding cron to renew cert to run ones per day ad midnight
echo "0 0 * * * renewcert.py" >> /etc/crontabs/root
crond -l 2 -f > /dev/stdout 2> /dev/stderr &

# start nginx so if new cert is needed the port 80 is ready for the challenge
nginx > /dev/stdout 2> /dev/stderr &

# Check for certificates
renewcert.py > /dev/stdout 2> /dev/stderr

# reload nginx
nginx -t && nginx -s reload > /dev/stdout 2> /dev/stderr

# initialize monitoring for new domains
monitor.py > /dev/stdout 2> /dev/stderr &

exec "$@"
