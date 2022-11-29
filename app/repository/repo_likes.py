from fastapi import HTTPException, status
from app.database.models.Likes import Likes
from app.database.models.Users import User

class RepoLikes:
    def __init__(self, session):
        self.session = session

    def getLikesCount(self, tweetid: int, user_id: int):
        likes = self.session.query(Likes).filter(Likes.tweet_id == tweetid).filter(Likes.user_id == user_id).count()
        return likes

    def checkLike(self, tweetid: int):
        likes = self.session.query(Likes).filter(Likes.tweet_id == tweetid).first()
        if not likes:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Like not found")

        return likes

    def createLike(self, tweetid: int, current_usr):
        user = self.session.query(User).filter(User.username == current_usr).first()
        like = Likes(likeBy=user.id, likeFrom=tweetid)
        self.session.add(like)
        self.session.commit()

        return like

    def deleteLike(self, tweetid):
        like = self.session.query(Likes).filter(Likes.likeFrom_id == tweetid).first()
        self.session.delete(like)
        self.session.commit()

        return like

    def getLikesByUser(self, likedBy: int, tweet_id: int):
        likes = self.db.query(Likes).filter(Likes.likeBy == likedBy).filter(Likes.likeOn == tweet_id).first()
        return likes