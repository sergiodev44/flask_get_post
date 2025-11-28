FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Install build deps for psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Make entrypoint executable
RUN chmod +x ./docker-entrypoint.sh

ENV FLASK_APP=unidad3_http.app:create_app
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["./docker-entrypoint.sh"]
