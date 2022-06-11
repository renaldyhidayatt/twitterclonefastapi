from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.config.database import Base

class Trends(Base):
    __tablename__ = "trends"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashtag = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    tweet_id = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return "<Trends(id='%s', hashtag='%s', user_id='%s', tweet_id='%s')>" % (self.id, self.hashtag, self.user_id, self.tweet_id)