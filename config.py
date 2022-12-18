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
