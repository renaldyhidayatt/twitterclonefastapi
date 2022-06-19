from ..repository.repo_retweet import RepoRetweet


class ServiceRetweet(RepoRetweet):
    def __init__(self, session):
        super().__init__(session)

    def getRetweetsCount(self, tweetid: int, user_id: int):
        retweets = super().getRetweetsCount(tweetid, user_id)
        return retweets

    def checkRetweet(self, tweetid: int, user_id: int):
        retweets = super().checkRetweet(tweetid, user_id)
        return retweets

    def createRetweet(self, tweetid: int, retweet, current_usr):
        retweet = super().createRetweet(tweetid, retweet.status)
        return retweet

    def getRetweets(self, tweetid: int):
        retweets = super().getRetweets(tweetid)
        return retweets

    def deleteRetweet(self, tweetid: int):
        retweet = super().deleteRetweet(tweetid)
        return retweet