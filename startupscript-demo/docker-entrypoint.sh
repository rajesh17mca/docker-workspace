#!/bin/sh
set -e

echo "Starting the Application...." >> /app/data/startup.log

exec "$@"