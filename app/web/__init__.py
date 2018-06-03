from app.web import web_bp
from app.util.log import logger

def init_module(app):
    logger.debug("%s init module start" % __name__)
    app.register_blueprint(web_bp)
    logger.debug("%s init module end" % __name__)
    

