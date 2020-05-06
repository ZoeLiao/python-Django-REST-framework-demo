#!/bin/bash

# Collects the static files from all installed apps and copies them to the STATICFILES_STORAGE.
python3 manage.py collectstatic --noinput

echo "migrate"
python3 manage.py migrate

# Start server
echo "Starting server"
nginx -g "daemon on;" && uwsgi --ini ./demo/uwsgi.ini
