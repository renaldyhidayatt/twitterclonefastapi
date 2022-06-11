from sqlalchemy import Column, Integer
from app.config.database import Base

class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    likeOn = Column(Integer, nullable=False)
    likeBy = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return "<Likes(id='%s', likeOn='%s', likeBy='%s')>" % (self.id, self.likeOn, self.likeBy)
