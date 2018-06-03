import os

class Config(object):
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', "jlsidlqidchuwldi12kdaokasidk")
    
