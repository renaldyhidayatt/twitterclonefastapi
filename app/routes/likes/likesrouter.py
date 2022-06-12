from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Likes import Likes
from app.database.models.Tweet import Tweet
from app.database.models.Users import User

from app.core.token import Token


router = APIRouter(prefix="/likes", tags=["Likes"])

@router.get("/getLikes/{tweet_id}")
def getLikesCount(tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    likes = db.query(Likes).filter(Likes.tweet_id == tweet_id).count()
    return likes


@router.post("/create/{tweet_id}")
def create(tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    likes = Likes(
        likeBy=user.id,
        likeOn=tweet_id,
    )
    db.add(likes)
    db.commit()

    return Response(status_code=status.HTTP_201_CREATED, content="Berhasil menyukai tweet")


@router.delete("/delete/{tweet_id}")
def delete(tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    likes = db.query(Likes).filter(Likes.likeBy == user.id).filter(Likes.likeOn == tweet_id).first()
    db.delete(likes)
    db.commit()

    return Response(status_code=status.HTTP_200_OK, content="Berhasil menghapus likes")


@router.get("/getLikesByUser/{likedBy}/{tweet_id}")
def getLikesByUser(likedBy: int, tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    likes = db.query(Likes).filter(Likes.likeBy == likedBy).filter(Likes.likeOn == tweet_id).first()
    return likes