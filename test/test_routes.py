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