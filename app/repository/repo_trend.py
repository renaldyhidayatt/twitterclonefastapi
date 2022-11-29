from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload

from ..database.models.Tweet import Tweet
from ..database.models.Users import User
from ..database.models.Trends import Trends
from app.schema.trends import TrendSchema

class RepoTrends:
    def __init__(self, session) -> None:
        self.session = session
    
    def trends(self):
        trend = self.session.query(Trends).options(joinedload(Trends.tweet)).all()
        return trend
    
    def create(self, trend: TrendSchema, twitter_id,current_usr: str):
        user = self.session.query(User).filter(User.username == current_usr).first()
        tweet = self.session.query(Tweet).filter(Tweet.id == twitter_id).first()

    
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
            )

        if not tweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Twitter"
            )

        trend = Trends(
            hashtag=trend.hashtag,
            user_id=user.id,
            tweet_id=tweet.id,
        )
        self.session.add(trend)
        self.session.commit()
        
        return trend

    def gettrend(self, trend_id):
        trend = self.session.query(Trends).options(joinedload(Trends.tweet)).filter(Trends.id == trend_id).first()
        if trend is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Trend not found"
            )
        return trend
    def countTrends(self, hashtag):
        trend = self.session.query(Trends).filter(Trends.hashtag == hashtag).count()
        return trend

    