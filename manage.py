from flask import Flask
from app import create_app
from flask_script import Manager, Shell
from app import db
from flask_migrate import Migrate, MigrateCommand
from app.models import Jieba_Word, Sentence

from werkzeug.contrib.cache import  MemcachedCache
app = create_app('default')

manager = Manager(app)

migrate = Migrate(app, db)

cache=MemcachedCache(['127.0.0.1:11211'])


def make_shell_context():
    dicts = {'app': app, 'db': db, 'sentence': Sentence,
             'word': Jieba_Word,
             }
    return dicts


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
