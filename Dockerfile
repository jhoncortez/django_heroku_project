# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2-binary \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D jhoncortez
USER jhoncortez

# run gunicorn FOR PRODUCTION ONLY
#CMD gunicorn djh_invoices_project.wsgi:application --bind 0.0.0.0:$PORT

# run python manage.py runserver  FOR DEVELOPMENT ONLY
CMD python manage.py runserver 0.0.0.0:$PORT

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]