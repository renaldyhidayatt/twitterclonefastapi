from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.utils.hashpassword import HashPassword
from app.utils.token import Token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.config.database import get_db
from .authschema import RegisterUser

from app.database.models.Users import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/")
async def hello():
    return "Hello"


@router.post("/register")
async def register(request: RegisterUser, db: Session = Depends(get_db)):
    db_user = User(
        firstName=request.firstName,
        lastName=request.lastName,
        username=request.username,
        email=request.email,
        password=HashPassword.create_hash(request.password),
    )
    db.add(db_user)
    db.commit()
    return Response(
        content="Berhasil membuat user", status_code=status.HTTP_201_CREATED
    )


@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    if not HashPassword.verify_hash(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = Token.create_access_token(data={"sub": user.username})
    response = {
        "firstName": user.firstName,
        "lastName": user.lastName,
        "username": user.username,
        "email": user.email,
        "jwtToken": access_token,
    }

    return response

@router.get("/getuser")
async def getUser(current_usr: str = Depends(Token.get_currentUser), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    
    response = {
        "name": user.name,
        "email": user.email,
    }

    return response