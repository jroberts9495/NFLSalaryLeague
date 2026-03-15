import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-123')

class DevelopmentConfig(Config):
    DEBUG = True