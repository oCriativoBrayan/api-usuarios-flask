import pytest 
#importo funcao do main
from main import create_app

#crio uma fixture (pre definicao)
@pytest.fixture
def app():
    #retorno chamando funcao crea...
    return create_app()

@pytest.fixture
def client(app):
    #retorno chamando
    return app.test_client()