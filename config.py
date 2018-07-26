# encoding=utf-8
import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to gess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_ADMIN = 'fjl2401@163.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    SQLALCHEMY_RECORD_QUERIES = True
    JSON_AS_ASCII = False

    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'fjl <fjl2401@163.com>'
    # FLASKY_POSTS_PER_PAGE = 5
    # FLASKY_USER_PER_PAGE = 10
    # FLASKY_COMMENTS_PRE_PAGE = 5
    # MAIL_SERVER = 'smtp.163.com'
    # MAIL_PORT = '25'
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('name_1')
    # MAIL_PASSWORD = os.environ.get('gpassword')

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'

    # SQLALCHEMY_DATABASE_URI = 'mysql://root:newpass@localhost:3306/shixun?charset=utf8mb4'

    @staticmethod
    def init_app(app):
        pass


class DevelopementConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABSE_URL') \
    #                           or 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:newpass@localhost:3306/shixun?charset=utf8mb4'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    DEBUG = True


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')


config = {
    'developement': DevelopementConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopementConfig,
}


#
class ProductionConfig(Config):
    pass


class UnixConfig(ProductionConfig):
    pass
