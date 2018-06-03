import os

env = os.getenv('FLASK_ENV', 'production')

if env == "production":
    from production import ProductionConfig
    config = ProductionConfig()
elif env == "development":
    from development import DevelopmentConfig
    config = DevelopmentConfig()
