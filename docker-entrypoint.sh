#!/bin/sh
set -e

echo "Waiting for Postgres at ${DB_HOST:-db}:${DB_PORT:-5432}..."
while ! python - <<'PY'
import os,sys
import psycopg2
try:
    psycopg2.connect(
        host=os.getenv('DB_HOST','db'),
        port=os.getenv('DB_PORT','5432'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        connect_timeout=3
    )
except Exception:
    sys.exit(1)
sys.exit(0)
PY
do
  echo "Postgres not ready - sleeping 1s"
  sleep 1
done

echo "Postgres is ready — starting Flask"
exec flask run --host=0.0.0.0 --port=5000
