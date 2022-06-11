from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.database.models import Tweet, Users

router = APIRouter(prefix="/tweet", tags=["Tweet"])

@router.get("/")
def tweets(db: Session = Depends(get_db)):
    tweet = db.query(Tweet).join(Users, Tweet.user_id == Users.id).join(Users, Tweet.tweetBy == Users.id).all()
    return tweet

@router.get("/gettweet")
def lom():
    pass
