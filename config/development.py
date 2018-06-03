import os
from config import Config

class DevelopmentConfig(Config):
    print "development config"
    DEBUG=True
