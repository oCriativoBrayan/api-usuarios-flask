from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/ping")
    def ping():
        return "pong"

    @app.route("/math")
    def math():
        return jsonify(result=8)
    
    return app