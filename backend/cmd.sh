#!/bin/bash

if [ "ENV" = "DEV"];then
  exec python /app/app.py
else
  exec uwsgi --http 7777 --wsgi-file /app/app.py --callable app
fi
