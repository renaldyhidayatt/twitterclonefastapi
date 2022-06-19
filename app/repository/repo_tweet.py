from fastapi import HTTPException, status

from ..database.models.Tweet import Tweet
from ..database.models.Users import User
from ..database.models.Trends import Trends
from sqlalchemy.orm import joinedload
from ..schema.tweet import TweetCreateSchema

class RepoTweet:
    def __init__(self, session) -> None:
        self.session = session

    def tweets(self):
        tweet = self.session.query(Tweet).options(joinedload(Tweet.tweetBy)).all()
        return tweet

    def tweetByMe(self, current_usr):
        user = self.session.query(User).filter(User.username == current_usr).first()
        tweet = self.session.query(Tweet).options(joinedload(Tweet.tweetBy)).\
            where(Tweet.tweetBy_id == user.id).order_by(Tweet.postedOn.desc()).all()

        return tweet

    def getTweetId(self, tweet_id):
        tweet = self.session.query(Tweet).filter(Tweet.id == tweet_id).first()
        if tweet is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Tweet not found"
            )
        return tweet

    def create(self, request: TweetCreateSchema, current_user):
        user = self.session.query(User).filter(User.username == current_user).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
            )

        tweet = Tweet(
            status=request.status,
            tweetBy_id=user.id,
        )
        self.session.add(tweet)
        self.session.commit()

        return tweet

    def countTweet(self, current_usr):
        tweet = self.session.query(Tweet).options(joinedload(Tweet.tweetBy)).filter(User.username == current_usr).count()
        return tweet
        
    def getHashtag(self, hashtag):
        tweet = self.session.query(Tweet).options(joinedload(Tweet.trends)).filter(Trends.hashtag == hashtag).order_by(Tweet.postedOn.desc()).all()
        if not tweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
            )
        return tweet

    # def getMention(self, current_user):
    #     user = self.session.query(User).filter(User.username == current_user).first()
    #     tweet = self.session.query(Tweet).options(joinedload(Tweet.tweetBy)).\
    #         where(Tweet.tweetBy_id == user.id).order_by(Tweet.postedOn.desc()).all()
    #     if not tweet:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
    #         )
    #     return tweet
    