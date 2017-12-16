import os


class Config:
    '''
    General configurations
    '''

class ProdConfig(Config):
    '''
    production configuration child class

    args:
        config: the parent class
    '''

    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI='sqlite:///database_sports.db'


class DevConfig(Config):
    '''
    Development configuration child class

    args:
        config: the parent class
    '''
    # SQLALCHEMY_DATABASE_URI='sqlite:///database_sports.db'
    SQLALCHEMY_DATABASE_URI='sqlite:///database_sports.db'

    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://chutha:chutha@localhost/sports_api'


    DEBUG = True
    # port = 3000

config_options={
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
