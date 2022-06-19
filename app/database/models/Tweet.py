from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Tweet(Base):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    tweetBy_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    tweetBy = relationship("User", back_populates="tweets")
    postedOn = Column(DateTime(timezone=True), default=func.now())
    trend = relationship("Trends", back_populates="tweet")
    retweet = relationship("Retweet", back_populates="retweetFrom")
    comment = relationship("Comment", back_populates="commentOn")
