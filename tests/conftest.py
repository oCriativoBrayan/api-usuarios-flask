#importo funcao do main
from app import create_app, db
import pytest

#crio uma fixture (pre definicao)
@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI":"sqlite:///:menory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

    #retorno chamando funcao crea...
    return create_app()

@pytest.fixture
def client(app):
    #retorno chamando
    return app.test_client()

#cria um fixture (automatizada)
@pytest.fixture
#define um funcao
def app_with_error():
    #cria um app
    app = create_app()

    #intancia um route
    @app.route("/erro500")
    def error500():
        #invoca um excecao
        raise Exception("simulated")
    #retorna o app
    return app

#cria um funcao erro 500, recebendo app da fixture
def test_500_route(app_with_error):
    client = app_with_error.test_client()
    response = client.get("/erro500")
    assert response.status_code == 500
    assert response.json["success"] is False
    assert response.json["error"] == "internal_error"


