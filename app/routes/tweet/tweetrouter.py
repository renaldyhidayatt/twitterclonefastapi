from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Tweet import Tweet
from app.database.models.Users import User
from app.database.models.Trends import Trends
from app.database.models.Follow import Follow

from app.utils.token import Token
from .tweetschema import TweetSchema

router = APIRouter(prefix="/tweet", tags=["Tweet"])

@router.get("/")
def tweets(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    tweet = db.query(Tweet).join(User, Tweet.tweetBy == User.id).filter(User.username == current_usr).all()
    return tweet

@router.get("/getweet/{id}")
def gettweet(id: int, current_usr: str = Depends(Token.get_currentUser), db: Session = Depends(get_db)):
    tweet = db.query(Tweet).join(User, Tweet.tweetBy == User.id).filter(Tweet.id == id).first()
    if tweet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tweet not found")
    
    return tweet

@router.post("/create")
def create(tweet: TweetSchema, current_usr: str = Depends(Token.get_currentUser) ,db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == current_usr).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    tweet = Tweet(
        status=tweet.status,
        tweetBy=user.id,
    )
    db.add(tweet)
    db.commit()
    return Response(
        content="Berhasil membuat tweet", status_code=status.HTTP_201_CREATED
    )

@router.get("/count")
def count(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    tweet = db.query(Tweet).filter(Tweet.tweetBy == user.id).count()
    return tweet


@router.get("/getHashtag/{hashtag}")
def getHashtag(hashtag: str, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(Tweet).join(Trends, Tweet.id == Trends.tweet_id).filter(Trends.hashtag == hashtag).order_by(Tweet.postedOn.desc()).all()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    return user

@router.get("/getMention")
def getMention(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(Tweet).join(User, Tweet.tweetBy == User.id).filter(User.username == current_usr).all()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    return user