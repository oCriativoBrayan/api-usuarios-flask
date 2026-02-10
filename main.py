from flask import Flask, jsonify

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
    
    return app