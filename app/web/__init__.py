from .web import web_bp

def init_module(app):
    print "%s init module start" % __name__
    app.register_blueprint(web_bp)
    print "%s init module end" % __name__
