from fastapi import APIRouter, Depends, status, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Retweet import Retweet
from app.database.models.Users import User
from app.routes.retweet.retweetschema import RetweetSchema

from app.utils.token import Token

router = APIRouter(prefix="/retweet", tags=["Retweet"])

@router.get("/getRetweetsCount/{tweetid}/{user_id}")
def getRetweetsCount(tweetid: int,user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    retweets = db.query(Retweet).filter(Retweet.tweet_id == tweetid).filter(Retweet.user_id == user_id).count()
    return retweets


@router.get("/checkRetweet/{tweetid}/{user_id}")
def checkRetweet(tweetid: int,user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    retweets = db.query(Retweet).filter(Retweet.tweet_id == tweetid).filter(Retweet.user_id == user_id).first()
    if not retweets:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retweet not found")

    return retweets


@router.post("/createRetweet/{tweetid}")
def createRetweet(tweetid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser),  retweet: RetweetSchema = Depends()):
    user = db.query(User).filter(User.id == current_usr).first()
    retweet = Retweet(retweetBy=user.id, retweetFrom=tweetid, status=retweet.status)
    db.add(retweet)
    db.commit()

    return retweet

@router.get("/getRetwet/{tweetid}")
def getRetweet(tweetid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    retweets = db.query(Retweet).filter(Retweet.tweet_id == tweetid).all()
    return retweets    