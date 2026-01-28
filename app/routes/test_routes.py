from app.models.user import User
from app.database import db
from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  # busca todos no banco
    return jsonify([user.to_dict() for user in users])

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