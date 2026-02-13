from flask import Blueprint, jsonify

math_bp = Blueprint("math", __name__)

@math_bp.route("/ping")
def ping():
    return "pong"

@math_bp.route("/math")
def math():
    return jsonify(result=8)

@math_bp.route("/soma")
def soma_route():
    from app.services.math_service import MathService
    service =  MathService()
    return jsonify(result=service.soma(5,5))
