import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    #SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = False
    MYSQL_HOST = 'database'
    MYSQL_USER = os.environ.get("MYSQL_USER")
    #MYSQL_PASSWORD = '123456'
    MYSQL_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
    MYSQL_DB = os.environ.get("MYSQL_DATABASE")


config = {
    'development': DevelopmentConfig
}
