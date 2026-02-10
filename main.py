from flask import Flask, jsonify, request
from app.services.math_service import soma

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
    
    return app