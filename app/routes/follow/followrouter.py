from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Follow import Follow
from app.database.models.Users import User

from app.utils.token import Token

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.get("/getFollowers/{followid}/{user_id}")
def getFollowers(followid: int,user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    followers = db.query(Follow).filter(Follow.sender == user_id).filter(Follow.receiver == followid).first()
    return followers


@router.post("/follow/{followid}")
def follow(followid: int,db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    follow = db.query(Follow).filter(Follow.sender == user.id).filter(Follow.receiver == followid).first()
    if not follow:
        follow = Follow(
            sender=user.id,
            receiver=followid,
        )
        db.add(follow)
        db.commit()
        return Response(
            content="Berhasil mengikuti", status_code=status.HTTP_201_CREATED
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )


@router.post("/unfollow/{followid}")
def unfollow(followid: int,db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    follow = db.query(Follow).filter(Follow.sender == user.id).filter(Follow.receiver == followid).first()
    if follow:
        db.delete(follow)
        db.commit()
        return Response(
            content="Berhasil mengikuti", status_code=status.HTTP_201_CREATED
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

@router.get("/addFollowCount")
def addFollowCount(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    user.followCount += 1
    db.commit()
    return Response(
        content="Berhasil mengikuti", status_code=status.HTTP_201_CREATED
    )

@router.get("/removeFollowCount")
def removeFollowCount(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    user.followCount -= 1
    db.commit()
    return Response(
        content="Berhasil mengikuti", status_code=status.HTTP_201_CREATED
    )


@router.get("/follwinglists")
def followinglists(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    followinglists = db.query(Follow).filter(Follow.sender == user.id).all()
    return followinglists

@router.get("/followerlists")
def followerlists(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    user = db.query(User).filter(User.username == current_usr).first()
    followerlists = db.query(Follow).filter(Follow.receiver == user.id).all()
    return followerlists


