from flask_sqlalchemy import SQLAlchemy
from app.util.log import logger

db = SQLAlchemy()

def init_module(app):
    logger.info("%s init module start" % __name__)
    db.init_app(app)
    logger.info("%s init module end" % __name__)