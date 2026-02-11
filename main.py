from flask import Flask, jsonify, request
from app.services.math_service import soma

class CustumError(Exception):
    pass

#define uma funcao
def create_app():
    #inicia um app
    app = Flask(__name__)
    
    #cria um route /ping
    @app.route("/ping")
    def ping():
        return "pong"

    #criaa um route /math
    @app.route("/math")
    def math():
        return jsonify(result=8)
    
    @app.route("/soma")
    def _soma():
        a, b = 5, 5
        return jsonify(result=soma(a, b))
    
    @app.errorhandler(404)
    def not_founf(error):
        return jsonify(success=False, error="not_found"), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify(success=False, error="internal_error"), 500
    
    @app.errorhandler(CustumError)
    def handle_custom_error(error):
        return jsonify(success=False, error=str(error)), 400
    
    return app