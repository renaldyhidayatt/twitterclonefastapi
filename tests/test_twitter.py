from .conftest import authclient

def test_alltwitter(authclient: authclient):
    response = authclient.get("/tweet/")
    assert response.status_code == 200
   

def test_getweetbyme(authclient: authclient):
    response = authclient.get("/tweet/tweetbyme")
    assert response.status_code == 200


def test_count(authclient: authclient):
    response = authclient.get("/tweet/count")
    assert response.status_code == 200


def test_tweetId(authclient: authclient, test_twitter):
    id = test_twitter["tweet"]["id"]
    response = authclient.get(f"/tweet/{id}")
    assert response.json()
    print(response.json())
    assert response.status_code == 200