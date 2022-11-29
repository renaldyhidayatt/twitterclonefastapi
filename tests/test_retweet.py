from .conftest import authclient

def test_checkRetweet(authclient: authclient, test_twitter):
    id = test_twitter["tweet"]["id"]
    response = authclient.get(f"/retweet/checkRetweet/{id}")
    assert response.json()
    print(response.json())
    assert response.status_code == 200


def test_getRetweetCount(authclient: authclient, test_twitter, test_user):
    id_twit = test_twitter["tweet"]["id"]
    id_user = test_user["user"]["id"]
    response = authclient.get(f"/retweet/getRetweetsCount/{id_twit}/{id_user}")
    
    print(response.json())
    assert response.status_code == 200

def test_deleteRetweet(authclient: authclient, test_twitter):
    id_twit = test_twitter["tweet"]["id"]
    response = authclient.delete(f"/retweet/deleteRetweet/{id_twit}")
    print(response.json())
    assert response.status_code == 200