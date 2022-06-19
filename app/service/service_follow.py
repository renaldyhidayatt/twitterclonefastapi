from ..repository.repo_follow import RepoFollow

class ServiceFollow(RepoFollow):
    def __init__(self, session):
        super().__init__(session)

    def checkFollow(self, sender: int, receiver: int):
        return super().checkFollow(sender, receiver)

    def followersList(self, current_usr):
        return super().followersList(current_usr)

    def followingList(self, current_usr):
        return super().followingList(current_usr)

    def follow(self, followid, current_usr):
        return super().follow(followid, current_usr)

    def unfollow(self, followid, current_usr):
        return super().unfollow(followid, current_usr)