import os
import sqlite3

class Config:
    """
    Common configuration
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    URL_ROOT = 'api'


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """
    Testing Configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///:memory:'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}

CONFIGURATION_NAME = os.environ.get('APP_CONFIG', 'testing')

if CONFIGURATION_NAME not in app_config:
    raise RuntimeError(f'Invalid configuration string {CONFIGURATION_NAME}')

config: Config = app_config[CONFIGURATION_NAME]()
