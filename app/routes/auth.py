import jwt
from flask import request, jsonify, current_app
from functools import wraps
from datetime import datetime, timedelta

def gerar_token(user_id):
   payload = {
      "user_id": user_id,
      "exp": datetime.utcnow() + timedelta(hours=1)
   }

   return jwt.encode(
       payload,
       current_app.config["SECRET_KEY"],
       algorithm="HS256"
   )

def token_required(f):
    @wraps(f)
    def decorated(usuario, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"erro": "Token ausente"}), 401
        
        try:
            token = auth_heards.split(" ")[1]
            payload = jwt.decode(
               token,
               current_app.config["SECRET_KEY"],
               algorithms =["HS256"]
            )

            usuarios = User.query.get(payload["user_id"])

            if not usuario:
               return jsonify({"erro":"Usuário não encontrado"}), 401
                 
        except:
            return jsonify({"erro": "Token inválido"}), 401
        
        return f(usuario, *args, **kwargs)
    
    return decorated