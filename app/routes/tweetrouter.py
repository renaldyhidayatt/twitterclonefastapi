from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.token import Token
from app.service.service_tweet import ServiceTweet
from ..schema.tweet import TweetSchema
from app.repository.repo_tweet import RepoTweet


router = APIRouter(prefix="/tweet", tags=["Tweet"])

@router.get("/")
def tweets(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceTweet(db)
        tweets = service.tweets()
        return tweets
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )
    

@router.get("/tweetbyme")
def tweet(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        repo = RepoTweet(db)
        tweet = repo.tweetByMe(current_usr)
        return tweet
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

@router.get("/count")
def count(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceTweet(db)
        tweet= service.countTweet(current_usr=current_usr)
    
        return tweet
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) 

@router.get("/{id}")
def getTweetId(id: int, current_usr: str = Depends(Token.get_currentUser), db: Session = Depends(get_db)):
    try:
        service = ServiceTweet(db)
        tweet = service.getTweetId(id)

        return tweet
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

@router.post("/create")
def create(request: TweetSchema, current_usr: str = Depends(Token.get_currentUser) ,db: Session = Depends(get_db)):
    try:

        service= ServiceTweet(db)
        service.create(request, current_usr)

        return Response(
            content="Berhasil membuat tweet", status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )




@router.get("/getHashtag/{hashtag}")
def getHashtag(hashtag: str, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:

        service = ServiceTweet(db)
        service.getHashtag(hashtag)

        return tweet
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))





# @router.get("/getMention")
# def getMention(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
#     repo = RepoTweet(db)
#     tweet = repo.getMention(current_usr)
#     return tweet

