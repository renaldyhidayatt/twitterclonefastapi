from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.config.database import Base

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String, nullable=False)
    messageTo = Column(Integer, nullable=False)
    messageFrom = Column(Integer, nullable=False)
    messageOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Messages(id='%s', message='%s', messageTo='%s', messageFrom='%s')>" % (self.id, self.message, self.messageTo, self.messageFrom)