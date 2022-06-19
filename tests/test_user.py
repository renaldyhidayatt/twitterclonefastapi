import json


def test_create_user(client):
    data = {
        "firstName": "dragon",
        "lastName": "kentang",
        "username": "testuser",
        "email": "testuser@nofoobar.com",
        "password": "testing",
    }
    response = client.post("/users/create", json.dumps(data))
    assert response.status_code == 201


def test_getuser(client, auth_user_tokenheader):
    response = client.get("/users/getuser", headers=auth_user_tokenheader)
    assert response.status_code == 200

