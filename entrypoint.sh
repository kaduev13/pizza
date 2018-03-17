#!/usr/bin/env sh

set -e

ENVIRONMENT="${ENVIRONMENT:-development}"

echo "Launching pizza-app with environment ${ENVIRONMENT}"

MIGRATIONS="python3 /code/manage.py migrate"
RUN_SERVER="/usr/local/bin/uwsgi --single-interpreter --enable-threads --ini /code/config/uwsgi.ini:${ENVIRONMENT}"

sleep 3

eval "${MIGRATIONS} && ${RUN_SERVER}"
