from flask import Flask
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    from app.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app