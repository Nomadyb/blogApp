FROM python:3.12.2-slim-bullseye
# FROM python:3.10.0a1-alpine3.12
# FROM python:3.10.0a7-alpine3.12



#Configure the server
COPY requirements.txt /app/requirements.txt


RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && pip install gunicorn




#Working directory
WORKDIR /app


ADD . .

EXPOSE 8000

# CMD [ "gunicorn","--bind",":8000","--workers","3","core.wsgi:application" ]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "core.wsgi:application"]



# CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
# CMD gunicorn core.wsgi:application --bind 0.0.0.0:8000
