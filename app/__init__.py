import os
import flask
import pkgutil
import sys
from flask_bootstrap import Bootstrap
from config import config

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
bootstrap = Bootstrap()

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(config)

    bootstrap.init_app(app)

    cur_path = []
    cur_path.append(os.path.abspath(os.path.dirname(__file__)))
    for _, name, is_pkg in pkgutil.iter_modules(cur_path):
        if is_pkg:
            module = __import__(name)
            if "init_module" in dir(module):
                module.init_module(app)
    return app
