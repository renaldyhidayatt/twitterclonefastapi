from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.token import Token
from app.service.service_tweet import ServiceTweet
from ..schema.tweet import TweetCreateSchema, TweetResponseSchema
from app.repository.repo_tweet import RepoTweet
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix="/tweet", tags=["Tweet"])

@router.get("/", response_model=List[TweetResponseSchema])
def tweets(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceTweet(db)
        tweets = service.tweets()
        
        
        return JSONResponse(content=jsonable_encoder(tweets), status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )
    

@router.get("/tweetbyme", response_model=List[TweetResponseSchema])
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
def create(request: TweetCreateSchema, current_usr: str = Depends(Token.get_currentUser) ,db: Session = Depends(get_db)):
    try:

        service= ServiceTweet(db)
        tweet= service.create(request, current_usr)

        response = {
            "message": "Successfully created tweet",
            "tweet": tweet
        }

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
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

