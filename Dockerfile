FROM python:3.12.2-slim-bullseye

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
COPY requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && pip install gunicorn

# Working directory
WORKDIR /app
ADD . .

# Collect static files
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "core.wsgi:application"]
