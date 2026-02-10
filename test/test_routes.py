def test_ping(client):
    response = client.get("/ping")
    assert response.data == b"pong"

def test_math(client):
    response = client.get("/math")

    assert response.status_code == 200
    assert response.json["result"] == 8