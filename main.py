from flask import Flask, jsonify, request
from app.services.math_service import soma

#instancia uma class  global, recebe uma excecao
class CustumError(Exception):
    #continua rodando
    pass

#define uma funcao
def create_app():
    #inicia um app, retornando um instancia nova
    app = Flask(__name__)
    
    #cria um route de teste simples /ping
    @app.route("/ping")
    def ping():
        return "pong"

    #cria um route de teste simples /math
    @app.route("/math")
    def math():
        return jsonify(result=8)
    
    #cria um route de teste simples /soma
    @app.route("/soma")
    def _soma():
        a, b = 5, 5
        return jsonify(result=soma(a, b))
    
    #cria um funcao captura o erro 404
    @app.errorhandler(404)
    #define uma funcao que recebe erro
    def not_founf(error):
        #retorna um json padrao
        return jsonify(success=False, error="not_found"), 404
    
 #cria um funcao captura o erro 500
    @app.errorhandler(500)
    #define uma funcao que recebe erro
    def internal_error(error):
        #retorna um json padrao
        return jsonify(success=False, error="internal_error"), 500
    

   #cria um funcao captura o erro customizado
    @app.errorhandler(CustumError)
    #define uma funcao que recebe erro customizado
    def handle_custom_error(error):
        ##retorna um json padrao
        return jsonify(success=False, error=str(error)), 400
    
    #retorna a instancia do app
    return app