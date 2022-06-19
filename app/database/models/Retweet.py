from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Retweet(Base):
    __tablename__ = "retweet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    retweetBy_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    retweetBy = relationship("User", back_populates="retweet")
    retweetFrom_id = Column(Integer, ForeignKey('tweet.id'),nullable=False)
    retweetFrom = relationship("Tweet", back_populates="retweet")
    status = Column(String, nullable=False)
    tweetOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Retweet(id='%s', retweetBy='%s', retweetFrom='%s', status='%s')>" % (self.id, self.retweetBy, self.retweetFrom, self.status)
