from main import CustumError

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

    assert response.status_code == 200

    assert response.json["result"] == 10



def test_404_route(client):
    response = client.get("/rota-inexistente")
    assert response.status_code == 404
    assert response.json['success'] is False
    assert response.json["error"] == "not_found"

def test_custom_error_route(client):
    from main import CustumError

    @client.application.route('/custom-error')
    def custom():
        raise CustumError('invalid_data')
    
    response = client.get('/custom-error')

    assert response.status_code == 400
    assert response.json['success'] is False
    assert response.json['error'] == 'invalid_data'

def test_500_route():
    from main import create_app
    app = create_app()

    @app.route('/erro500')
    def error500():
        raise Exception("simulated")
    
    client = app.test_client()
    response = client.get("/erro500")
    assert response.status_code == 500
    assert response.json["success"] is False
    assert response.json["error"] == 'internal_error'


