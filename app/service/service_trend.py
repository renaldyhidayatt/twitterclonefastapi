from ..repository.repo_trend import RepoTrends
from ..schema.trends import TrendSchema


class ServiceTrends(RepoTrends):
    def __init__(self, session) -> None:
        super().__init__(session)

    def trends(self):
        return super().trends()

    def create(self, trend: TrendSchema, current_usr: str):
        return super().create(trend, current_usr)

    def gettrend(self, trend_id):
        return super().gettrend(trend_id)
