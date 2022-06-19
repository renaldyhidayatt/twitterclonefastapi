from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Follow import Follow
from app.database.models.Users import User
from ..service.service_follow import ServiceFollow

from app.core.token import Token

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.get("/getFollowers/{followid}/{user_id}")
def getFollowers(followid: int,user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceFollow(db)
        follow = service.getFollowers(followid,user_id)
        return follow
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.post("/follow/{followid}")
def follow(followid: int,db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceFollow(db)
        service.follow(followid,current_usr)
        return Response(
            content="Berhasil mengikuti", status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.post("/unfollow/{followid}")
def unfollow(followid: int,db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceFollow(db)
        service.unfollow(followid,current_usr)
        return Response(
            content="Berhasil tidak mengikuti", status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



@router.get("/follwinglists")
def followinglists(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceFollow(db)
        follow = service.followersList(current_usr)
        return follow

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.get("/followerslists")
def followerslists(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceFollow(db)
        follow = service.followersList(current_usr)
        return follow

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )



