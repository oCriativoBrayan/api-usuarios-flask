import sys
import os

# Ajuste de path para projeto sem estrutura formal
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import create_app #chama para test factory
from app.services.user_services import _test_math #chama funcao teste calculo

#teste de calculo
def test_math():
    assert _test_math(8, 2) == 16

#teste da factory
def test_multiply_route():
    app = create_app()
    client = app.test_client()

    response = client.get("/_test_math")

    assert response.status_code == 200
    assert response.json["result"] == 16


