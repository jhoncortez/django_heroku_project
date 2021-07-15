#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

## creating essential apps for project (crete once)
# python manage.py startapp authentication
# python manage.py startapp clients
# python manage.py startapp invoices

# only execute once at beginnig of project
# python manage.py flush --no-input
# python manage.py makemigrations clients
# python manage.py makemigrations invoices
# python manage.py migrate

exec "$@"