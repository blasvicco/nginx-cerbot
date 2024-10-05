FROM nginx:alpine

ENV ESSENTIAL_PACKAGES="busybox-openrc py-pip python3" \
    UTILITY_PACKAGES="mlocate vim"

RUN apk update && \
    apk --no-cache --progress add $ESSENTIAL_PACKAGES $UTILITY_PACKAGES

# Installing cerbot
RUN pip3 install certbot --break-system-packages && \
    pip3 install inotify-simple --break-system-packages

# Copy scripts
COPY ./data/scripts/entrypoint.sh /usr/bin/entrypoint.sh
COPY ./data/scripts/monitor.py /usr/bin/monitor.py
COPY ./data/scripts/newcert.sh /usr/bin/newcert.sh
COPY ./data/scripts/renewcert.py /usr/bin/renewcert.py

WORKDIR /home/www

ENTRYPOINT ["entrypoint.sh"]
