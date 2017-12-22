import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True

class ReleaseConfig(BaseConfig):
    DEBUG = True

configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
    'release': ReleaseConfig
}