from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.database.models.Users import User
from app.core.database import get_db
from app.core.hashpassword import HashPassword
from app.core.token import Token
from sqlalchemy.orm import Session
from app.repository.repo_user import RepoUser
from app.schema.user import UserCreateSchema, UserResponseSchema, UserUpdateSchema
from app.service.service_user import ServiceUser

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/hello")
async def hello():
    return "Hello"




@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    try:
        service = ServiceUser(db)
        users = service.getusers()
        return users

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

@router.post("/create")
async def create(request: UserCreateSchema, db: Session = Depends(get_db)):
    try:

        service = ServiceUser(db)
        service.createuser(request)
        return Response(
            content="Berhasil membuat user", status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.get("/getuser", response_model=UserResponseSchema)
async def getUser(current_usr: str = Depends(Token.get_currentUser), db: Session = Depends(get_db)):
    try:

        service = ServiceUser(db)
        user = service.get_username(current_usr)
    
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



@router.get("/{username}", response_model=UserResponseSchema)
async def getUsername(username: str, current_user: str = Depends(Token.get_currentUser),db: Session = Depends(get_db)):
    try:
        service = ServiceUser(db)
        user = service.get_username(username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
            )

        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

@router.put("/update")
async def update(request: UserUpdateSchema, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:

        service = ServiceUser(db)
        service.updateuser(request, current_usr)
    
        return Response(status_code=status.HTTP_200_OK, content="Berhasi; update user")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

@router.delete("/delete")
async def delete(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:

        service = ServiceUser(db)
        service.deleteuser(current_usr)

        return Response(status_code=status.HTTP_200_OK, content="Berhasil menghapus user")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )