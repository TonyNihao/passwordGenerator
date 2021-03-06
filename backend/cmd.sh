#!/bin/bash

set -e

if [ "$ENV" = "DEV" ];then
  exec python /app/app.py
elif [ "$ENV" = "UNIT" ];then
  exec python /app/tests.py
else
  exec uwsgi --http 0.0.0.0:7777 --wsgi-file /app/app.py --callable app
fi
