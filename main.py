from flask import Flask, request, jsonify
from app.services.user_services import _test_math, create_user #erro por nao importa create_user aqui

def create_app():
    app = Flask(__name__)

    @app.route("/_test_math")
    def multiply_route():
        return jsonify(result=_test_math(8, 2)), 200

    return app