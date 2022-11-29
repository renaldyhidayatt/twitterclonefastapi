from fastapi import APIRouter, Depends, status, HTTPException, Response
from requests import Response
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.schema.retweets import RetweetSchema
from app.service.service_retweet import ServiceRetweet
from app.core.token import Token

router = APIRouter(prefix="/retweet", tags=["Retweet"])

@router.get("/getRetweetsCount/{tweetid}/{user_id}")
def getRetweetsCount(tweetid: int,user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceRetweet(db)
        return service.getRetweetsCount(tweetid, user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

@router.get("/checkRetweet/{tweetid}")
def checkRetweet(tweetid: int,db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceRetweet(db)
        return service.checkRetweet(tweetid)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.post("/createRetweet/{tweetid}")
def createRetweet(retweet: RetweetSchema,tweetid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceRetweet(db)
        return service.createRetweet(tweetid, retweet, current_usr)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



@router.delete("/deleteRetweet/{tweetid}")
def deleteRetweet(tweetid: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceRetweet(db)
        service.deleteRetweet(tweetid)
        return Response(status=status.HTTP_200_OK, content="Retweet deleted")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )