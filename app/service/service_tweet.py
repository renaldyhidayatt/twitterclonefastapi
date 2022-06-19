
from ..repository.repo_tweet import RepoTweet
from ..schema.tweet import TweetSchema


class ServiceTweet(RepoTweet):
    def __init__(self, session):
        super().__init__(session)
    
    def tweets(self):
        return super().tweets()
    
    def tweetByMe(self, current_usr):
        return super().tweetByMe(current_usr)

    def getTweetId(self, tweet_id):
        return super().getTweetId(tweet_id)

    def create(self, request: TweetSchema, current_user):
        return super().create(request, current_user)

    def countTweet(self, current_usr):
        return super().countTweet(current_usr)
    
    def getHashtag(self, hashtag):
        return super().getHashtag(hashtag)

    # def getMention(self, current_user):
    #     return super().getMention(current_user)