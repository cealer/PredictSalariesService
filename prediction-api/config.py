import os

class Config(object):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = False
