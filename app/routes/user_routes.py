import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

#define o blueprint de usuários
user_bp = Blueprint('user_bp', __name__)

#pasta para salvar uploadscd
UPLOAD_FOLDER = 'uploads/'

#tipos de arquivos permitidos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'nef'}

#valida se o arquivo tem uma extensão permitida
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@user_bp.route('/users', methods=['POST'])
def upload_user():

    #pega o arquivo de imagem do request
    image = request.files.get('image')

    #verifica se imagem não está vazia  
    if image is None or image.filename == '':
        return jsonify({"Error": "imagem obrigatória"}), 400

    #verifica se o formato da imagem é permitido
    if not allowed_file(image.filename):
        return jsonify({"Error": "formato de imagem inválido"}), 400    
    
    #garante que o nome do arquivo é seguro
    filename = secure_filename(image.filename)

    #define o caminho completo para salvar a imagem
    path = os.path.join(UPLOAD_FOLDER, filename)

    #salva a imagem na pasta de uploads
    image.save(path)

    print("METHOD:", request.method)
    print("FILES:", request.files)
    print("FORM:", request.form)
    
    return jsonify({
        "success": True,
        "filename": filename
    }), 200

    