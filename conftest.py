#importo funcao do main
from main import create_app
import pytest

#crio uma fixture (pre definicao)
@pytest.fixture
def app():
    #retorno chamando funcao crea...
    return create_app()

@pytest.fixture
def client(app):
    #retorno chamando
    return app.test_client()

@pytest.fixture
def app_with_error():
    app = create_app()

    @app.route("/erro500")
    def error500():
        raise Exception("simulated")
    
    return app

def test_500_route(app_with_error):
    client = app_with_error.test_client()
    response = client.get("/erro500")
    assert response.status_code == 500
    assert response.json["success"] is False
    assert response.json["error"] == "internal_error"


