from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Tweet import Tweet
from app.database.models.Users import User
from app.database.models.Trends import Trends
from .trendschema import TrendSchema
from app.core.token import Token

router = APIRouter(prefix="/trends", tags=["Trends"])

@router.get("/")
def trends(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    trend = db.query(Trends).all()
    return trend


@router.post("/create")
def create(trend: TrendSchema, current_usr: str = Depends(Token.get_currentUser),db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == current_usr).first()
    tweet = db.query(Tweet).filter(Tweet.tweetBy == user.id).first()

  
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    trend = Trends(
        hashtag=trend.hashtag,
        user_id=user.id,
        tweet_id=tweet.id,
    )
    db.add(trend)
    db.commit()
    return Response(
        content="Berhasil membuat trend", status_code=status.HTTP_201_CREATED
    )


@router.get("/count")
def count(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    trend = db.query(Trends).filter(Trends.user_id == user.id).count()
    return trend


