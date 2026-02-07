from flask import Flask, request, jsonify
from app.error import register_error_handlers
from app.routes.user_routes import user_bp
from app.logger import setup_logger
from app.services.health_service import get_health

import time

app = Flask(__name__)

logger = setup_logger()
app.logger.handlers = logger.handlers
app.logger.setLevel(logger.level)

register_error_handlers(app)  

app.register_blueprint(user_bp, url_prefix="/users")



@app.route("/health")
def health():
    return get_health()

@app.route("/math")
def count():
    return jsonify(result= 8 * 2)

@app.before_request
def start_time():
    request.start_time = time.time()

def create_app():
    return "ok"


@app.after_request
def log_request(response):
    duration = time.time() - request.start_time

    app.logger.info(
        f"{request.method} {request.path}"
        f"{response.status_code}"
        f"{duration:.3f}s"
    )

    return response

@app.route("/ping")
def ping():
    return {"ok": True}


if __name__ == '__main__':
    app.run(debug=True)
