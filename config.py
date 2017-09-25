'''config.py'''

import os


class Config(object):
    '''Config base class'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Place super secret app key here'

    @staticmethod
    def init_app(app):
        '''Initialise app'''
        pass


class DevelopmentConfig(Config):
    '''Development config'''
    DEBUG = True


class ProductionConfig(Config):
    '''Production config'''
    pass


class TestingConfig(Config):
    '''Testing config'''
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': ProductionConfig
}
