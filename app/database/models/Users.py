from sqlalchemy import Column, Integer, String
from app.config.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    profileImage = Column(String, nullable=False, default="defaultProfilePic.png")
    profileCover = Column(String, nullable=False, default="backgroundCoverPic.svg")
    bio = Column(String, nullable=True)
    country = Column(String, nullable=True)
    website = Column(String, nullable=True)

    