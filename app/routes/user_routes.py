from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def upload_test():

    print("FORM:", request.form)
    print("FILES:", request.files)

    image = request.files.get('image')

    if image is None:
        return jsonify({"error": "imagem não chegou"}), 400

    return jsonify({
        "success": True,
        "filename": image.filename
    }), 200

