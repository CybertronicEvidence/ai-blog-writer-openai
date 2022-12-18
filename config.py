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
