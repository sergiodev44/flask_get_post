import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER","uploads/")


class DevConfig(Config):
    DEBUG = True
    # SECRET_KEY = "123"

class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = "456"