#!/bin/sh

# Adding cron to renew cert to run ones per day ad midnight
echo "0 0 * * * renewcert.py" >> /etc/crontabs/root
crond -l 2 -f > /dev/stdout 2> /dev/stderr &

# start nginx so if new cert is needed the port 80 is ready for the challenge
nginx &

# Check for certificates
renewcert.py

# reload nginx
nginx -t && nginx -s reload

exec "$@"
