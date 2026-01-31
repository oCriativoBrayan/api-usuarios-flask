from flask import jsonify
import logging

logger = logging.getLogger("api")

def register_error_handlers(app):

    @app.errorhandler(500)
    def internal_error(e):
        logger.error("Erro 500", exc_info=True)
        return jsonify({
            "success": False,
            "error": "Erro interno do servidor"
        }), 500
