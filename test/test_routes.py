def test_ping(client):
    response = client.get("/ping")
    assert response.data == b"pong"

def test_math(client):
    #instancia client
    response = client.get("/math")
    #teste retorno status
    assert response.status_code == 200
    #test retorno resultado
    assert response.json["result"] == 8

def test_soma(client):
    response = client.get("/soma")

    #valida retorno starus processamento
    assert response.status_code == 200
    
    #valida retorno contrato json
    assert response.json["result"] == 10


#cria uma funcao de test erro
def test_404_route(client): #recebe client
    
    #faz requisicao get rota
    response = client.get("/rota-inexistente")

    #valida retorno status
    assert response.status_code == 404
    #valida retorno json
    assert response.json['success'] is False
    #valida conteudo do erro
    assert response.json["error"] == "not_found"

#cria uma funcao test customizado erro
def test_custom_error_route(client):

    #importa class global do main
    from main import CustumError

    #cria um route temporario intermamente
    @client.application.route('/custom-error')

    #cria funcao route
    def custom():
        #invoca um excecao
        raise CustumError('invalid_data')
    
    #faz requisicao get rota
    response = client.get('/custom-error')

    #valida retorno status
    assert response.status_code == 400
    #valida retorno json
    assert response.json['success'] is False
    #valida conteudo do erro
    assert response.json['error'] == 'invalid_data'

#cria um app isolado
def test_500_route():
    #importa funcao do main, criar instancias isoladas
    from main import create_app

    #cria app
    app = create_app()
    
    #cria um route temporario intermamente
    @app.route('/erro500')
    def error500():
        #invoca um excecao
        raise Exception("simulated")
    
    #simula uma requisicao HTTP real
    client = app.test_client()
    #faz requisicao get rota
    response = client.get("/erro500")
    #valida retorno status
    assert response.status_code == 500
    #valida retorno json
    assert response.json["success"] is False
    #valida conteudo do erro
    assert response.json["error"] == 'internal_error'


def test_soma_mocked(client, monkeypatch):
    #cria funcao fake
    def fake_soma(a, b):
        return 999
    
    #substitui soma real pela fake
    monkeypatch.setattr(
        "main.soma",
        fake_soma
    )

    response = client.get('/soma')

    assert response.status_code == 200
    assert response.json['result'] == 999