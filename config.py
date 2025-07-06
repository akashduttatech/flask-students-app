class Config(object):
    DEBUG = True
    TESTING = False
    
    SECRET_KEY = 'f1a8b6bce17c401b81ae324e9d1a420ba1a9e2c7fd3b56b8b33e3e473ac1b65d'
    
    DB_NAME = 'flask_crud_app'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_HOST = 'localhost'

    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SESSION_COOKIE_SECURE = True



class ProductionConfig(Config):
    pass



class DevelopmentConfig(Config):
    DEBUG = True
    
    SESSION_COOKIE_SECURE = False


    
class TestingConfig(Config):
    TESTING = True
    
    SESSION_COOKIE_SECURE = False