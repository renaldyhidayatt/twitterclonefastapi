from datetime import datetime, timedelta
from jwt import PyJWTError, encode, decode
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import Settings



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class Token:

    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = encode(to_encode, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)
        return encoded_jwt

    def verify_token(token: str, credentials_exception):
        try:
            payload = decode(token, Settings.SECRET_KEY, algorithms=Settings.ALGORITHM)
            email: str = payload.get("sub")

            if email is None:
                raise credentials_exception
            token_data = email

            

            return token_data;
        except PyJWTError:
            raise credentials_exception

    def get_currentUser(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        return Token.verify_token(
            token=data, credentials_exception=credentials_exception
        )