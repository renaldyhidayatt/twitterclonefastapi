from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.hashpassword import HashPassword

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


    def __repr__(self):
        return "<User(id='%s', firstName='%s', lastName='%s', username='%s', email='%s', password='%s', profileImage='%s', profileCover='%s', bio='%s', country='%s', website='%s')>" % (self.id, self.firstName, self.lastName, self.username, self.email, self.password, self.profileImage, self.profileCover, self.bio, self.country, self.website)

    
    def setPassword(self):
        self.password = HashPassword.create_hash(self.password)

    def checkPassword(self, password) -> bool:
        return HashPassword.verify_hash(self.password, password)
    