from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.routes.auth.authschema import RegisterUser
from app.database.models.Users import User
from app.core.database import get_db
from app.core.hashpassword import HashPassword
from app.core.token import Token
from sqlalchemy.orm import Session
from .userschema import UserSchema

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/create")
async def create(request: RegisterUser, db: Session = Depends(get_db)):
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

@router.get("/")
async def getAll(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/getuser")
async def getUser(current_usr: str = Depends(Token.get_currentUser), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    
    response = {
        "firstName": user.firstName,
        "lastName": user.lastName,
        "username": user.username,
        "email": user.email,
        "profileImage": user.profileImage,
        "profileCover": user.profileCover,
        "bio": user.bio,
        "country": user.country,
        "website": user.website,
    }

    return response

@router.get("/getuser/{username}")
async def getUserByUsername(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    response = {
        "firstName": user.firstName,
        "lastName": user.lastName,
        "username": user.username,
        "email": user.email,
        "profileImage": user.profileImage,
        "profileCover": user.profileCover,
        "bio": user.bio,
        "country": user.country,
        "website": user.website,
    }

    return response

@router.put("/update")
async def update(request: UserSchema, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    user.firstName = request.firstName
    user.lastName = request.lastName
    user.username = request.username
    user.email = request.email
    user.password = HashPassword.create_hash(request.password)
    user.profileImage = request.profileImage
    user.profileCover = request.profileCover
    user.bio = request.bio
    user.country = request.country
    user.website = request.website

    db.commit()
    return Response(status_code=status.HTTP_200_OK, content="Berhasil mengubah user")


@router.delete("/delete")
async def delete(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    db.delete(user)
    db.commit()
    return Response(status_code=status.HTTP_200_OK, content="Berhasil menghapus user")