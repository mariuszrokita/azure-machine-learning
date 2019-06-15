#!/bin/bash
echo "Running app in production mode!"
exec uwsgi --ini app.ini