from flask import Flask, request
from app.error import register_error_handlers
from app.routes.user_routes import user_bp
from app.logger import setup_logger
import time

app = Flask(__name__)

logger = setup_logger()
app.logger.handlers = logger.handlers
app.logger.setLevel(logger.level)

register_error_handlers(app)  

app.register_blueprint(user_bp, url_prefix="/users")

def health_check():
    return True

@app.before_request
def start_time():
    request.start_time = time.time()


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
