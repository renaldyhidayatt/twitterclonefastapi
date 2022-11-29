from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Follow(Base):
    __tablename__ = "follow"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(Integer, ForeignKey('user.id'),nullable=False)
    receiver = Column(Integer, ForeignKey("user.id"),nullable=False)
    followOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Follow(id='%s', sender='%s', receiver='%s', followStatus='%s')>" % (self.id, self.sender, self.receiver, self.followStatus)