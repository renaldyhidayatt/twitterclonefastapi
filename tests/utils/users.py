
from fastapi import status, HTTPException
from fastapi.testclient import TestClient
from app.repository.repo_user import RepoUser
from sqlalchemy.orm import Session


def user_authenticate_headers(client: TestClient, username: str, password: str):
    data = {
        "username": username,
        "password": password
    }
    r = client.post("/auth/login", data=data)
    print(r.json())
    response = r.json()
    auth_token = response["jwtToken"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers

def authTokenFromEmail(client: TestClient, username: str, db: Session):
    password = "testing"
    user = RepoUser(db).get_username(username=username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    return user_authenticate_headers(client=client, username=username, password=password)