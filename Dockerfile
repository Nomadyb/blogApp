FROM python:3.12.2-slim-bullseye
# FROM python:3.10.0a1-alpine3.12
# FROM python:3.10.0a7-alpine3.12

COPY requirements.txt /app/requirements.txt

#Configure the server
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt



#Working directory
WORKDIR /app


ADD . .

# EXPOSE 8000

# CMD [ "gunicorn","--bind",":8000","--workers","3","core.wsgi:application" ]

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT