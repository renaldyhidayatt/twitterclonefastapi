from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Trends(Base):
    __tablename__ = "trend"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashtag = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"),nullable=False)
    user = relationship("User")
    tweet_id = Column(Integer, ForeignKey("tweet.id"),nullable=False)
    tweet = relationship("Tweet", back_populates="trend")
    

    def __repr__(self) -> str:
        return "<Trends(id='%s', hashtag='%s', user_id='%s', tweet_id='%s')>" % (self.id, self.hashtag, self.user_id, self.tweet_id)