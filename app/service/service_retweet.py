from ..repository.repo_retweet import RepoRetweet
from ..schema.retweets import RetweetSchema

class ServiceRetweet(RepoRetweet):
    def __init__(self, session):
        super().__init__(session)

    def getRetweetsCount(self, tweetid: int, user_id: int):
        retweets = super().getRetweetsCount(tweetid, user_id)
        return retweets

    def checkRetweet(self, tweetid: int):
        retweets = super().checkRetweet(tweetid)
        return retweets

    def createRetweet(self, tweetid: int, retweet: RetweetSchema, current_usr):
        return super().createRetweet(tweetid, retweet, current_usr)
   

    def deleteRetweet(self, tweetid: int):
        retweet = super().deleteRetweet(tweetid)
        return retweet