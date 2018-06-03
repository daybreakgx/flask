import os
import sys
import pkgutil
from app.util.log import logger

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
def init_module(app):
    logger.debug("%s init module start" % __name__)
    cur_path = []
    cur_path.append(os.path.abspath(os.path.dirname(__file__)))
    for _, name, is_pkg in pkgutil.iter_modules(cur_path):
        if is_pkg:
            module = __import__(name)
            if "init_module" in dir(module):
                module.init_module(app)
    logger.debug("%s init module end" % __name__)
