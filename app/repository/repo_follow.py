from fastapi import status, HTTPException, Response
from app.database.models.Follow import Follow
from app.database.models.Users import User
from sqlalchemy.orm import joinedload


class RepoFollow:
    def __init__(self, session):
        self.session = session
    
    def checkFollow(self, sender: int, receiver: int):
        follow = self.session.query(Follow).filter(Follow.sender == sender).filter(Follow.receiver == receiver).first()
        if follow:
            return True
        else:
            return False
    
    def followingList(self, current_usr):
        following = self.session.query(Follow).options(joinedload(Follow.receiver)).all()

        return following

    def followersList(self, current_usr):
        followers = self.session.query(Follow).options(joinedload(Follow.sender)).all()

        return followers

    def follow(self, followid, current_usr):
        user = self.session.query(User).filter(User.username == current_usr).first()
        follow = self.session.query(Follow).filter(Follow.sender == user.id).filter(Follow.receiver == followid).first()
        if not follow:
            follow = Follow(
                sender=user.id,
                receiver=followid,
            )
            self.session.add(follow)
            self.session.commit()
            return Response(
                content="Berhasil mengikuti", status_code=status.HTTP_201_CREATED
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Follow"
            )
            
    def unfollow(self, followid, current_usr):
        user = self.session.query(User).filter(User.username == current_usr).first()
        follow = self.session.query(Follow).filter(Follow.sender == user.id).filter(Follow.receiver == followid).first()
        if follow:
            self.session.delete(follow)
            self.session.commit()
            return Response(
                content="Berhasil tidak mengikuti", status_code=status.HTTP_201_CREATED
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Unfollow"
            )

    
    def getFollowers(self, followid, user_id: int):
        followers = self.session.query(Follow).filter(Follow.sender == user_id).filter(Follow.receiver == followid).first()
        return followers

    