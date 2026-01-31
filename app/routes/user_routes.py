from flask import Blueprint, request, jsonify
from app.models.user import User
from app.database import db
import os

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/boom')
def boom():
    return jsonify({"message": "Boom!"})


@user_bp.route('/users', methods=['POST'])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    image = request.files.get('image')

    if not name or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    filename = None
    if image:
        os.makedirs('uploads', exist_ok=True)
        filename = image.filename
        image.save(os.path.join('uploads', filename))

    user = User(name=name, email=email, image=filename)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])
