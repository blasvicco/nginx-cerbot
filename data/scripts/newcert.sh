#!/bin/sh
domain=$1
certbot certonly \
--webroot --webroot-path /home/www/certbot/ \
--non-interactive \
--agree-tos \
--email $CERTBOT_EMAIL \
--keep-until-expiring \
--preferred-challenges=http \
--cert-name $domain \
-d $domain > /dev/stdout 2> /dev/stderr
