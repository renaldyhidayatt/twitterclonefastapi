from ..repository.repo_likes import RepoLikes


class ServiceLikes(RepoLikes):
    def __init__(self, session):
        super().__init__(session)

    def createLike(self, tweetid: int, current_usr):
        return super().createLike(tweetid, current_usr)

    def getLikesCount(self, tweetid: int, user_id: int):
        return super().getLikesCount(tweetid, user_id)

    def checkLike(self, tweetid: int):
        return super().checkLike(tweetid)

    def deleteLike(self, tweetid: int):
        return super().deleteLike(tweetid)
    
    def getLikesByUser(self, likedBy: int, tweet_id: int):
        return super().getLikesByUser(likedBy, tweet_id)