from fastapi.encoders import jsonable_encoder
from .conftest import authclient
import json

def test_all_trends(authclient: authclient):
    response = authclient.get("/trends/")
    assert response.status_code == 200
    print(response.json())


def test_create_trend(authclient: authclient, test_twitter):
    id = test_twitter["tweet"]["id"]
    data = {
        "hashtag": "mytest"
    }
    response = authclient.post(f"/trends/create/{id}", json.dumps(data))
    assert response.status_code == 201


def test_count_trend(authclient: authclient):
    response = authclient.get("/trends/count/mytest")
    assert response.status_code == 200