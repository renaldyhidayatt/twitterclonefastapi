from sqlalchemy.orm import Session
from ..repository.repo_likes import RepoLikes


class ServiceLikes(RepoLikes):
    def __init__(self, session: Session):
        self.likes_repository = RepoLikes(session)

    def createLike(self, tweetid: int, current_usr):
        return self.likes_repository.createLike(tweetid, current_usr)

    def getLikesCount(self, tweetid: int, user_id: int):
        return self.likes_repository.getLikesCount(tweetid, user_id)

    def checkLike(self, tweetid: int):
        return self.likes_repository.checkLike(tweetid)

    def deleteLike(self, tweetid: int):
        return self.likes_repository.deleteLike(tweetid)
    
    def getLikesByUser(self, likedBy: int, tweet_id: int):
        return self.likes_repository.getLikesByUser(likedBy, tweet_id)