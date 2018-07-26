# encoding=utf-8
from flask import Flask, render_template, redirect, url_for, session, flash
# from flask_moment import Moment
from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from config import config

# from flask_pagedown import PageDown
# from redis import Redis
# import rq
# import logging
# from logging.handlers import RotatingFileHandler
import os

dir_name = os.path.dirname(__file__)
bootstrap = Bootstrap()
db = SQLAlchemy()


# 工厂函数
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
