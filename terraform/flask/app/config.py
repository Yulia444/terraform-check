import os
from dotenv import load_dotenv

# load_dotenv()


class Config():
    FLASK_APP = os.getenv('FLASK_APP')
    SECRET_KEY = "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('RDS_USERNAME')}:{os.getenv('RDS_PASSWORD')}@{os.getenv('RDS_HOST')}/{os.getenv('RDS_DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    DEBUG=True


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
       