from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    commentBy_id = Column(Integer, ForeignKey("user.id"),nullable=False)
    commentBy = relationship("User", back_populates="comment")
    commentOn_id = Column(Integer, ForeignKey("tweet.id"),nullable=False)
    commentOn = relationship("Tweet", back_populates="comment")
    comment = Column(String, nullable=False)
    commentAt = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Comment(id='%s', commentBy='%s', commentOn='%s', comment='%s')>" % (self.id, self.commentBy, self.commentOn, self.comment)