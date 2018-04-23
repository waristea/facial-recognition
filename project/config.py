import os
basedir = os.path.abspath(os.path.dirname(__file__))

local = 'postgresql:///waristea'
remote = 'postgres://rdhyoptimnimte:a82b1f413c7602658e8e866f6121bd43c7ff2609c3d99517715f7a29c286706f@ec2-54-83-204-6.compute-1.amazonaws.com:5432/d11d9t87a4vu0q'

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'f:$\x80\xac\xc3\xb6\x07\x84\x8bL\x06\x14\x17\xfe\t\x85^\xa3\xbf)\r\x19V'
    SQLALCHEMY_DATABASE_URI = remote

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
