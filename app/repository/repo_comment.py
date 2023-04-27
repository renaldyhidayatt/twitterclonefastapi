from fastapi import status, Response
from sqlalchemy.orm import joinedload, Session
from app.database.models.Comment import Comment
from app.database.models.Users import User

class RepoComment:
    def __init__(self, session: Session) -> None:
        self.session = session


    def getComments(self, tweetid: int):
        comments = self.session.query(Comment).options(joinedload(Comment.commentBy)).filter(Comment.commentOn_id == tweetid).all()

        return comments

    def wasCommentBy(self, commentBy: int, commentOn: int):
        comments = self.session.query(Comment).options(joinedload(Comment.commentBy)).filter(Comment.commentBy_id == commentBy).filter(Comment.comment_on == commentOn).first()
        
        return comments

    def createComment(self, tweetid: int, comment: Comment, current_user: str):
        user = self.session.query(User).filter(User.id == current_user).first()
        comment = Comment(commentBy_id=user.id, commentOn_id=tweetid, comment=comment.comment)
        self.session.add(comment)
        self.session.commit()

        return Response(status_code=status.HTTP_201_CREATED, detail="Comment created")

    def deleteComment(self, commentid: int):
        comment = self.session.query(Comment).filter(Comment.id == commentid).first()

        self.session.delete(comment)
        self.session.commit()

        return Response(status_code=status.HTTP_200_OK, detail="Comment deleted")