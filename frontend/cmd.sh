#!/bin/bash
set -e


if [ "ENV" = "DEV" ];then
  exec python /app/app.py
else
  exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/app.py --callable app
fi
