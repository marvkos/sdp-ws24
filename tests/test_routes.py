def test_route(client):
    response = client.get('/notfound')

    assert response.status_code == 404
