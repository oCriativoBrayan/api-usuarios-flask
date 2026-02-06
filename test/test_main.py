import sys
import os


# Ajuste de path para projeto sem estrutura formal
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import health_route, ping, app

def test_after_request_loggind():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

def test_health_route():
    assert health_route() == "ok"

def test_ping():
    assert ping() == {"ok": True}

