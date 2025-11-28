import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "mi_nd_db")
    DB_USER = os.getenv("DB_USER", "myuser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER","uploads/")

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = "456"


# # run app
# source venv/bin/activate
# export FLASK_APP=unidad3_http.app:create_app
# export FLASK_ENV=development
# flask run --host=127.0.0.1 --port=5000


# # Truncate tables and restart the app so init_db() will seed
# PGPASSWORD=1234 psql -h localhost -U myuser -d mi_nd_db -c "TRUNCATE TABLE products, users RESTART IDENTITY CASCADE;"
# # then restart your Flask app (or start it with these env vars)
# source venv/bin/activate
# export DB_USER=myuser DB_PASSWORD=1234 DB_NAME=mi_nd_db DB_HOST=localhost DB_PORT=5432
# export FLASK_APP=unidad3_http.app:create_app
# export FLASK_ENV=development
# flask run --host=127.0.0.1 --port=5000