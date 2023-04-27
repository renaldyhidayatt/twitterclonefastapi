from sqlalchemy.orm import Session
from ..repository.repo_follow import RepoFollow

class ServiceFollow(RepoFollow):
    def __init__(self, session: Session) -> None:
       self.follow_repository = RepoFollow(session=session)

    def checkFollow(self, sender: int, receiver: int):
        return self.follow_repository.checkFollow(sender=sender, receiver=receiver)

    def followersList(self, current_usr):
        return self.follow_repository.followersList(current_usr)

    def followingList(self, current_usr):
        return self.follow_repository.followingList(current_usr)

    def follow(self, followid, current_usr):
        return self.follow_repository.follow(followid, current_usr)

    def unfollow(self, followid, current_usr):
        return self.follow_repository.unfollow(followid, current_usr)

    def getFollowers(self, followid, user_id: int):
        return self.follow_repository.getFollowers(followid, user_id)