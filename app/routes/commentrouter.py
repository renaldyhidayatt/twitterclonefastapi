from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.token import Token
from app.database.models.Comment import Comment
from ..schema.comment import CommentResponseSchema, CommentSchema
from app.database.models.Users import User
from ..service.service_comment import ServiceComment

router = APIRouter(prefix="/comment", tags=["Comment"])


@router.get("/getComments/{tweetid}", response_model=List[CommentResponseSchema])
def getComments(tweetid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceComment(db)
        comment = service.getComments(tweetid)
        return comment

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.get("/wasCommentBy/{commentBy}/{commentOn}")
def wasCommentBy(commentBy: int, commentOn: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceComment(db)
        comment = service.wasCommentBy(commentBy,commentOn)
        return comment
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.post("/createComment/{tweetid}")
def createComment(tweetid: int, comment: CommentSchema, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceComment(db)
        service.createComment(tweetid,comment,current_usr)
        return Response(status_code=status.HTTP_201_CREATED, detail="Comment created")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



@router.delete("/deleteComment/{commentid}")
def deleteComment(commentid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceComment(db)
        service.deleteComment(commentid)
        return Response(status_code=status.HTTP_200_OK, detail="Comment deleted")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )
