from flask import jsonify
import logging

logger = logging.getLogger("api")

def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error("Verifica o tipo", exc_info=True)
        
        return {
            "success": False,
            "error": "Erro interno"
        }, 500