from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.config.database import Base

class Tweet(Base):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    tweetBy = Column(Integer, ForeignKey("user.id"), nullable=False)
    postedOn = Column(DateTime(timezone=True), default=func.now())
