from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.config.database import Base

class Retweet(Base):
    __tablename__ = "retweet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    retweetBy = Column(Integer, nullable=False)
    retweetFrom = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    tweetOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Retweet(id='%s', retweetBy='%s', retweetFrom='%s', status='%s')>" % (self.id, self.retweetBy, self.retweetFrom, self.status)
