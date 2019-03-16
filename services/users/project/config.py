class BaseConfig:
    """Base configs"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configs"""
    pass

class TestingConfig(BaseConfig):
    """Testing configs"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass