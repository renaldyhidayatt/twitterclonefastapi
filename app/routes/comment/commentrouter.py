from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.utils.token import Token
from app.database.models.Comment import Comment
from .commentschema import CommentSchema
from app.database.models.Users import User

router = APIRouter(prefix="/comment", tags=["Comment"])


@router.get("/getComments/{tweetid}")
def getComments(tweetid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    comments = db.query(Comment).filter(Comment.tweet_id == tweetid).all()
    return comments


@router.get("/wasCommentBy/{commentBy}/{commentOn}")
def wasCommentBy(commentBy: int, commentOn: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    comments = db.query(Comment).filter(Comment.comment_by == commentBy).filter(Comment.comment_on == commentOn).first()
    if not comments:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    return comments


@router.post("/createComment/{tweetid}")
def createComment(tweetid: int, comment: CommentSchema, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.id == current_usr).first()
    comment = Comment(comment_by=user.id, comment_on=tweetid, comment=comment.comment)
    db.add(comment)
    db.commit()

    return Response(status_code=status.HTTP_201_CREATED, detail="Comment created")


@router.delete("/deleteComment/{commentid}")
def deleteComment(commentid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    comment = db.query(Comment).filter(Comment.id == commentid).first()
    if not comment:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    db.delete(comment)
    db.commit()

    return Response(status_code=status.HTTP_200_OK, detail="Comment deleted")