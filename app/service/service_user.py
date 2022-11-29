from ..repository.repo_user import  RepoUser


class ServiceUser(RepoUser):
    def __init__(self, session):
        super().__init__(session)
    
    def getusers(self):
        return super().getAll()

    def getusername(self, username):
        return super().get_username(username)

    def updateuser(self, username, request):
        return super().updateuser(username, request)

    def deleteuser(self, username):
        return super().deleteUser(username)

    
