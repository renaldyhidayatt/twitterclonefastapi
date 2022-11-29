from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String, nullable=False)
    messageTo = Column(Integer, ForeignKey('user.id'),nullable=False)
    messageFrom = Column(Integer, ForeignKey('user.id'),nullable=False)
    messageOn = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Messages(id='%s', message='%s', messageTo='%s', messageFrom='%s')>" % (self.id, self.message, self.messageTo, self.messageFrom)