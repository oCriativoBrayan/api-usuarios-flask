from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.math_routes import math_bp
from app.errors.handlers import register_error_handlers

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    #verifica status db
    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    #registra blueprint
    app.register_blueprint(math_bp)

    #registra handlers
    register_error_handlers(app)

    return app
