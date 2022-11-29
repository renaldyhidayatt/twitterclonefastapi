import pytest
from typing import Any, Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from app.core.database import Base, get_db
from app.core.token import Token
from app.routes.main import main_router

def start_application():
    app = FastAPI()
    app.include_router(main_router)

    return app


SQLALCHEMY_DATABASE_URL = "sqlite:///./twitter_test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def app() -> Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)  # Create the tables.
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="module")
def session(app: FastAPI):
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionTesting()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client(
    app: FastAPI, session: SessionTesting
) -> Generator[TestClient, Any, None]:
   

    def _get_test_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def test_user(client: TestClient):
    user_data = {
        "firstName": "Test",
        "lastName": "User",
        "username": "testuser",
        "email": "dargon@gmail.com",
        "password": "testpassword",
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    new_user = response.json()
    print(new_user)

    return new_user


@pytest.fixture(scope="module")
def token(test_user):
    return Token.create_access_token(data={"sub": test_user["user"]["username"]})


@pytest.fixture(scope="module")
def authclient(client: TestClient, token):
    client.headers = {"Authorization": f"Bearer {token}"}
    return client


@pytest.fixture(scope="module")
def test_twitter(authclient: authclient):
    twitter_data = {
        "status": "test tweet",
    }
    response = authclient.post("/tweet/create", json=twitter_data)
    assert response.status_code == 201
    new_twitter = response.json()
    print(new_twitter)

    return new_twitter

@pytest.fixture(scope="module")
def test_retweet(authclient: authclient, test_twitter):
    id = test_twitter["tweet"]["id"]
    response = authclient.post(f"/retweet/createRetweet/{id}")
    assert response.json()
    print(response.json())
    assert response.status_code == 200
    return response.json()