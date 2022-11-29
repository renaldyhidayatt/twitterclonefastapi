from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Likes import Likes
from app.database.models.Users import User

from app.core.token import Token
from app.service.service_likes import ServiceLikes


router = APIRouter(prefix="/likes", tags=["Likes"])

@router.get("/getLikes/{tweet_id}")
def getLikesCount(tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceLikes(db)
        return service.getLikesCount(tweet_id, current_usr)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.post("/create/{tweet_id}")
def create(tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceLikes(db)
        service.create(tweet_id, current_usr)
        return Response(status_code=status.HTTP_201_CREATED, content="Berhasil menyukai tweet")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.delete("/delete/{tweet_id}")
def unLike(tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    
    try:
        service = ServiceLikes(db)
        service.deleteLike(tweet_id)
        return Response(status_code=status.HTTP_200_OK, content="Berhasil unlikes tweet tersebut")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



@router.get("/getLikesByUser/{likedBy}/{tweet_id}")
def getLikesByUser(likedBy: int, tweet_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceLikes(db)
        return service.getLikesByUser(likedBy, tweet_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )