from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    profileImage = Column(String, nullable=True, default="defaultProfilePic.png")
    profileCover = Column(String, nullable=True, default="backgroundCoverPic.svg")
    bio = Column(String, nullable=True)
    country = Column(String, nullable=True)
    website = Column(String, nullable=True)
    tweets = relationship("Tweet", back_populates="tweetBy")
    retweet = relationship("Retweet", back_populates="retweetBy")
    comment = relationship("Comment", back_populates="commentBy")


    