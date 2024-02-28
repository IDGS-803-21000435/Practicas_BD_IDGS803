import os
import urllib
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'Clave_Nueva'
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/practica_flask_BD'
    SQLALCHEMY_TRACK_MODIFICATION = False