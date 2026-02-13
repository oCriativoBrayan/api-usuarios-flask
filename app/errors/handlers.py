from flask import jsonify
from app.models.user import db, User


class CustomError(Exception):
    pass

def test_create_user(app):
    with app.app_context():
        user = User(name="Brayan")
        db.session.add(user)
        db.session.commit()

        saved = User.query.first()

        assert saved.name == "Brayan"

def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(success=False, error="not_found"), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify(success=False, error="internal_error"), 500
    
    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        return jsonify(success=False, error=str(error)), 400
    
    