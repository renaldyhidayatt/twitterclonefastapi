from ..repository.repo_trend import RepoTrends
from ..schema.trends import TrendSchema


class ServiceTrends(RepoTrends):
    def __init__(self, session) -> None:
        super().__init__(session)

    def trends(self):
        return super().trends()

    def create(self, trend: TrendSchema, twitter_id,current_usr: str):
        return super().create(trend, twitter_id,current_usr)

    def gettrend(self, trend_id):
        return super().gettrend(trend_id)

    def countTrends(self, hashtag):
        return super().countTrends(hashtag)
