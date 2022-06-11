from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.config.database import Base

class Tweet(Base):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    tweetBy = Column(Integer, nullable=False)
    postedOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Tweet(id='%s', status='%s', tweetBy='%s')>" % (self.id, self.status, self.tweetBy)