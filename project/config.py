import os
basedir = os.path.abspath(os.path.dirname(__file__))

local = 'postgresql:///waristea'
remote = 'postgres://uianwaxtvpyccm:b72b679a63da331d81b8a96be17f5970eeb7f14f3f66613c6020e95847023f3c@ec2-174-129-41-64.compute-1.amazonaws.com:5432/d3o81pejgsvb56'

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
