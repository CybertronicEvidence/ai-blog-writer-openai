##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
