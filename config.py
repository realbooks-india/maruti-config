
# connection = 'mysql+pymysql://root:Ams1234@localhost/flasktest'
# connection = 'mysql+pymysql://root:Aman@1234@localhost/pythonmis'

class Config:
    # SECRET_KEY = 'ams1234567890ams'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nj30103@localhost/maruti_1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    # SECRET_KEY = 'ams1234567890ams'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nj30103@172.20.0.2/maruti_1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Config):
    # SECRET_KEY = 'ams1234567890ams'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nj30103@3.7.47.250/maruti'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # SECRET_KEY = 'ams1234567890ams'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nj30103@172.20.0.2/maruti'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
