from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({
       "sucess": True,
        "data": [],
        "message": "List of users"
    })

@user_bp.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({"error": "Content-type must be application/json"}), 415

    data = request.get_json()   

    name = data.get("name")
    email = data.get("email")

    return jsonify({
        "success": True,
        "name": name,
        "email": email 

    }), 201

