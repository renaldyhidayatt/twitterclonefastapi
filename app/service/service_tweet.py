from sqlalchemy.orm import Session
from ..repository.repo_tweet import RepoTweet
from ..schema.tweet import TweetSchema


class ServiceTweet(RepoTweet):
    def __init__(self, session: Session):
        self.tweet_repository = RepoTweet(session)
    
    def tweets(self):
        return self.tweet_repository.tweets()
    
    def tweetByMe(self, current_usr):
        return self.tweet_repository.tweetByMe(current_usr)

    def getTweetId(self, tweet_id):
        return self.tweet_repository.getTweetId(tweet_id)

    def create(self, request: TweetSchema, current_user):
        return self.tweet_repository.create(request, current_user)

    def countTweet(self, current_usr):
        return self.tweet_repository.countTweet(current_usr)
    
    def getHashtag(self, hashtag):
        return self.tweet_repository.getHashtag(hashtag)

    # def getMention(self, current_user):
    #     return super().getMention(current_user)