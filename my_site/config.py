class Config(object):
		DEBUG = False
		TESTING = False
		SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True


