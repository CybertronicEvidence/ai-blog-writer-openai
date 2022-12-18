##OPEN API STUFF
OPENAI_API_KEY = "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"



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
