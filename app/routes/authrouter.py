from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.core.hashpassword import HashPassword
from app.core.token import Token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.database import get_db
from app.schema.user import UserCreateSchema
from app.service.service_user import ServiceUser

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/")
async def hello():
    return "Hello"


@router.post("/register")
async def register(request: UserCreateSchema, db: Session = Depends(get_db)):
    try:
        service = ServiceUser(db)
        user = service.createuser(request)
        
        response = {
            "message": "Successfully created user",
            "user": user
        }
        json_ = jsonable_encoder(response)

        return JSONResponse(
            content=json_,
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        service = ServiceUser(db)
        user = service.get_username(request.username)
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
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

