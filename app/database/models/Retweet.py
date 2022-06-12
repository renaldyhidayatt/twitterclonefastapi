from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Retweet(Base):
    __tablename__ = "retweet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    retweetBy = Column(Integer, ForeignKey('user.id'),nullable=False)
    retweetFrom = Column(Integer, ForeignKey('tweet.id'),nullable=False)
    status = Column(String, nullable=False)
    tweetOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Retweet(id='%s', retweetBy='%s', retweetFrom='%s', status='%s')>" % (self.id, self.retweetBy, self.retweetFrom, self.status)
