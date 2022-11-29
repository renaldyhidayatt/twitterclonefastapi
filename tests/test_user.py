from fastapi.testclient import TestClient

def test_user_create(client: TestClient):
    data = {
        "firstName": "John",
        "lastName": "Doe",
        "username": "johndoe",
        "email": "johndoe@gmail.com",
        "password": "dota2"
    }
    response = client.post("/auth/register", json=data)
    assert response.status_code == 201


def test_getuser(authclient: TestClient):
    response = authclient.get("/users/getuser")
    assert response.status_code == 200

def test_get_allUser(authclient: TestClient):
    response = authclient.get("/users")
    assert response.status_code == 200


def test_get_username(authclient: TestClient, test_user):
    response = authclient.get(f"/users/{test_user['user']['username']}")
    
    assert response.status_code == 200
   

def test_user_update(authclient: TestClient):
    response = authclient.put("/users/update", json={
        "firstName": "django",
        "lastName": "flask",
        "username": "master",
        "email": "dargon",
        "password": "dargon",
        "profileImage": "dargon.png",
        "profileCover": "dargonposter.png",
        "bio": "as",
        "country": "dragon",
        "website": "postaot"
    })
    assert response.status_code == 200


# def test_user_delete(authclient: TestClient):
#     response = authclient.delete("/users/delete")
#     assert response.status_code == 200