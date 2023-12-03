def test_request_example(client):
    response = client.get("/")
    assert b"<h1>Hello, World!</h1>" in response.data
