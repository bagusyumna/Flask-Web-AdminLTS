import os

class Config:
    SECRET_KEY = '437b4477c9d3a375f31c9101f5222766'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tesappkurniawan@gmail.com'
    MAIL_PASSWORD = 'Tesapp4321'