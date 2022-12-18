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
