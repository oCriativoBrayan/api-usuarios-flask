import sys
import os

# Ajuste de path para projeto sem estrutura formal
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

def test_after_request_loggind():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

def test_math_route():
    client = app.test_client()
    response = client.get("/math")

    assert response.status_code == 200
    assert response.json["result"] == 16



def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_ping():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200


