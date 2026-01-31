from flask import Flask, jsonify
from app.routes.user_routes import user_bp
from app.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

@app.errorhandler(500)
def internal_error(e):
    logger.error("Erro 500 capturado", exc_info=True)
    return jsonify({
        "success": False,
        "error": "Erro interno do servidor"
    }), 500

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=False)
