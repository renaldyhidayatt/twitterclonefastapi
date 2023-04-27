from sqlalchemy.orm import Session
from ..repository.repo_trend import RepoTrends
from ..schema.trends import TrendSchema


class ServiceTrends(RepoTrends):
    def __init__(self, session:Session) -> None:
        self.trends_repository = RepoTrends(session)

    def trends(self):
        return self.trends_repository.trends()

    def create(self, trend: TrendSchema, twitter_id,current_usr: str):
        return self.trends_repository.create(trend, twitter_id,current_usr)

    def gettrend(self, trend_id):
        return self.trends_repository.gettrend(trend_id)

    def countTrends(self, hashtag):
        return self.trends_repository.countTrends(hashtag)
