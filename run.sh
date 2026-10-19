#!/bin/sh
set -eu

if docker container inspect parceldesk-ca4 >/dev/null 2>&1; then
    docker rm -f parceldesk-ca4
fi

docker run -d --name parceldesk-ca4 -p 8080:8000 \
    -e APP_MDOE=production parceldesk:ca4
