from flask import Blueprint, request # type: ignore
from app.services.user_services import list_users, find_user, create_user # type: ignore
from app.utils.response import success_response, error_response # type: ignore

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users')
def get_users():
    return success_response(list_users())

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        return success_response(find_user(user_id))
    except ValueError as e:
        return error_response(str(e), 404)
    

@user_bp.route('/users', methods=['POST'])
def create():
    if not request.is_json:
        return error_response("Envie JSON", 400)

    try:
        return success_response(
            create_user(request.json),
            "Usuário criado",
            201
        )
    except ValueError as e:
        return error_response(str(e), 400)
