"""
  Main configurations for the api
"""


class Config(object):
    """Main Configurations class"""

    DEBUG = False
    SECRET_KEY = "dbjkkhdh87373gg36t3gwd26"
    ENV = "development"


class DevelopmentConfig(Config):
    """Developement environment configurations"""

    DEBUG = True


class TestingConfig(Config):
    """testing environment configurations"""
    FLASK_ENV = "testing"
    DEBUG = True


class StagingConfig(Config):
    """staging environment configurations"""

    DEBUG = True


class ProductionConfig(Config):
    """Production environment configurations"""

    DEBUG = False


secret_key = Config.SECRET_KEY

app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
