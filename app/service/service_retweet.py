from sqlalchemy.orm import Session

from ..repository.repo_retweet import RepoRetweet
from ..schema.retweets import RetweetSchema

class ServiceRetweet(RepoRetweet):
    def __init__(self, session: Session):
        self.retweet_repository = RepoRetweet(session)

    def getRetweetsCount(self, tweetid: int, user_id: int):
        retweets = self.retweet_repository.getRetweetsCount(tweetid, user_id)
        return retweets

    def checkRetweet(self, tweetid: int):
        retweets = self.retweet_repository.checkRetweet(tweetid)
        return retweets

    def createRetweet(self, tweetid: int, retweet: RetweetSchema, current_usr):
        return self.retweet_repository.createRetweet(tweetid, retweet, current_usr)
   

    def deleteRetweet(self, tweetid: int):
        retweet = self.retweet_repository.deleteRetweet(tweetid)
        return retweet