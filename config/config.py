import os

class Config(object):
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', "jlsidlqidchuwldi12kdaokasidk")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.0.106/flask"
