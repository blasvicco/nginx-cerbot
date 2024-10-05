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

RUN addgroup --gid 1000 app-user && \
    adduser --disabled-password --no-create-home --gecos "" --home /home/www --ingroup app-user --uid 1000 app-user && \
    addgroup app-user nginx

WORKDIR /home/www

ENTRYPOINT ["entrypoint.sh"]
