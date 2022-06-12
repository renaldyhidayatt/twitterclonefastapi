from sqlalchemy import Column, ForeignKey, Integer
from app.core.database import Base

class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    likeOn = Column(Integer, ForeignKey('user.id'),nullable=False)
    likeBy = Column(Integer, ForeignKey('tweet.id'),nullable=False)

    def __repr__(self) -> str:
        return "<Likes(id='%s', likeOn='%s', likeBy='%s')>" % (self.id, self.likeOn, self.likeBy)
