from app.models.user import User
from app.database import db
from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "usuário não encontrado"}), 404

    return jsonify(user.to_dict()), 200

@user_bp.route('/users', methods=['POST'])         
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    image = request.files.get('image')

    if not name or not email:
        return jsonify('{"Error": "Nome e email são obrigatórios"}'), 400
    
    filename = None
    if image:
        filename = image.filename
        image.save(f'uploads/{filename}')
    
    user = User(
        name=name,
        email=email,
        image=filename
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201

@user_bp.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "usuário não encontrado"}), 404

    data = request.form

    if 'name' in data:
        user.name = data.get('name')

    if 'email' in data:
        user.email = data.get('email')

    image = request.files.get('image')
    if image:
        user.image = image.filename
        image.save(f'uploads/{image.filename}')

    db.session.commit()

    return jsonify(user.to_dict()), 200



@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "usuário não encontrado"}), 404
    
    data = request.form

    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Nome e email são obrigatórios"}), 400
    
    user.name =  data.get('name')
    user.email = data.get('email')

    db.session.commit()

    return jsonify(user.to_dict()), 200