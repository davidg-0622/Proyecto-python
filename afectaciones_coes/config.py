# config.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/afectaciones_coes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_PKG_TYPE = 'full'
