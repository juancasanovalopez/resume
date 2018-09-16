#!/bin/sh
source matrix/bin/activate
flask db upgrade
flask translate compile
exec gunicorn -b 8000:5000 --access-logfile - --error-logfile - resume:app