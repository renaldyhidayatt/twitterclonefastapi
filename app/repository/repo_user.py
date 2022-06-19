from fastapi import HTTPException, status

from app.schema.user import UserCreateSchema, UserUpdateSchema

from ..database.models.Users import User
from app.core.hashpassword import HashPassword


class RepoUser:
    def __init__(self, session):
        self.session = session

    def createuser(self, request: UserCreateSchema) -> User:
        db_user = User(
            firstName=request.firstName,
            lastName=request.lastName,
            username=request.username,
            email=request.email,
            password=HashPassword.create_hash(request.password),
        )
        self.session.add(db_user)
        self.session.commit()

        return db_user
    
    def get_username(self, username):
        user = self.session.query(User).filter(User.username == username).first()
       
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
            )

        return user

    def getAll(self) -> User:
        return self.session.query(User).all()

    def updateuser(self, username,request: UserUpdateSchema) -> User:
        user = self.get_username(username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
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

        self.session.commit()


        return user

    def deleteUser(self, username):
        user = self.get_username(username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
            )
        
        self.session.delete(user)
        self.session.commit()

        return "Delete"
    