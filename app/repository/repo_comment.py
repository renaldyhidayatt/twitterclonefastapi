from fastapi import HTTPException, status, Response
from sqlalchemy.orm import joinedload
from app.database.models.Comment import Comment
from app.database.models.Users import User

class RepoComment:
    def __init__(self, session) -> None:
        self.session = session


    def getComments(self, tweetid: int):
        comments = self.session.query(Comment).options(joinedload(Comment.commentBy)).filter(Comment.commentOn_id == tweetid).all()

        return comments

    def wasCommentBy(self, commentBy: int, commentOn: int):
        comments = self.session.query(Comment).options(joinedload(Comment.commentBy)).filter(Comment.commentBy_id == commentBy).filter(Comment.comment_on == commentOn).first()

        if not comments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

        return comments

    def createComment(self, tweetid: int, comment: Comment, current_user: str):
        user = self.db.query(User).filter(User.id == current_user).first()
        comment = Comment(commentBy_id=user.id, commentOn_id=tweetid, comment=comment.comment)
        self.session.add(comment)
        self.session.commit()

        return Response(status_code=status.HTTP_201_CREATED, detail="Comment created")

    def deleteComment(self, commentid: int):
        comment = self.session.query(Comment).filter(Comment.id == commentid).first()
        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

        self.session.delete(comment)
        self.session.commit()

        return Response(status_code=status.HTTP_200_OK, detail="Comment deleted")