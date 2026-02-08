import sys
import os

# Ajuste de path para projeto sem estrutura formal
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app, _test_math #chama funcao math

#realiza test de usuario valido, inserindo usuario manualmente
def test_create_user_success():
    client = app.test_client()

    response = client.post(
        "/_test_users",
        json={
            "name": "Test",
            "email": "test@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json["user"]["name"] == "Test"
    assert response.json["user"]["email"] == "test@example.com"

#test cadastro do usuario, com dados invalidos
def test_create_user_invalid_data():
    client = app.test_client()

    response = client.post(
        "/_test_users",
        json={
            "name": "Marcos"
        }
    )

    assert response.status_code == 400
    assert "error" in response.json



def test_multiply_route():
    assert _test_math(8, 2) == 16

def test_math_route():
    client = app.test_client()
    response = client.get("/test_math")

    assert response.status_code == 200
    assert response.json["result"] == 16


def test_ping():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200


