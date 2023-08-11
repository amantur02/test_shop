#!/bin/sh
echo "Waiting for postgres..."

while ! nc -z "${POSTGRES_HOST}" "${POSTGRES_PORT}"; do
  sleep 0.1
done
echo "PostgreSQL started"

echo "Migrate the Database at startup of project"
python3 manage.py migrate

echo "Running uvicorn"
python3 manage.py runserver