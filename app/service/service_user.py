from sqlalchemy.orm import Session
from ..repository.repo_user import  RepoUser


class ServiceUser(RepoUser):
    def __init__(self, session: Session):
        self.user_repository = RepoUser(session)
    
    def getusers(self):
        return self.user_repository.getAll()

    def getusername(self, username):
        return self.user_repository.get_username(username)

    def updateuser(self, username, request):
        return self.user_repository.updateuser(username, request)

    def deleteuser(self, username):
        return self.user_repository.deleteUser(username)

    
