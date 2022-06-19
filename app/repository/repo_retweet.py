from app.database.models.Retweet import Retweet
from app.database.models.Users import User
from app.schema.retweets import RetweetSchema
from fastapi import HTTPException, status


class RepoRetweet:
    def __init__(self, session) -> None:
        self.session = session

    def getRetweetsCount(self,tweetid: int, user_id: int):
        retweets = self.db.query(Retweet).filter(Retweet.tweet_id == tweetid).filter(Retweet.user_id == user_id).count()
        return retweets

    def checkRetweet(self,tweetid: int):
        retweets = self.db.query(Retweet).filter(Retweet.tweet_id == tweetid).first()
        if not retweets:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retweet not found")

        return retweets

    def createRetweet(self,tweetid: int,  retweet: RetweetSchema, current_usr):
        user = self.query(User).filter(User.username == current_usr).first()
        retweet = Retweet(retweetBy=user.id, retweetFrom=tweetid, status=retweet.status)
        self.db.add(retweet)
        self.db.commit()

        return retweet

    def deleteRetweet(self, tweetid):
        retweet = self.db.query(Retweet).filter(Retweet.retweetFrom_id == tweetid).first()
        self.db.delete(retweet)
        self.db.commit()

        return retweet