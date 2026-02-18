from flask import Blueprint, jsonify, request
from app.routes.auth import gerar_token, token_required

bp = Blueprint("main", __name__)

@bp.route("/usuarios", methods=["POST"])
def criar_usuarios():
    return jsonify({"msg":"usuario criado"}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.getjson()

    usuario = User.query.filter_by(email=data["email"]).first()

    if not usuario or not usuario.check_senha(data["senha"]):
        return jsonify({"erro":"Credencias inválidas"}), 401
    
    token = gerar_token(usuario.id)
    
    return jsonify({"token": token})


@bp.route("/perfil")
@token_required
def perfil(usuario):
    return jsonify({
        "id": usuario.id,
        "email": usuario.email
    })