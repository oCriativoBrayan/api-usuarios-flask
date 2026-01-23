from flask import Flask
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)

    #registra o blueprint de usuários
    app.register_blueprint(user_bp)

    return app

if __name__ == '__main__':
        app = create_app()
        app.run(debug=True)