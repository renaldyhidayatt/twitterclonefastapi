from sqlalchemy.orm import Session
from ..repository.repo_message import RepoMessage
from ..schema.messages import MessageSchema

class ServiceMessage(RepoMessage):
    def __init__(self, session: Session) -> None:
        self.message_repository = RepoMessage(session)
        
    def getMessages(self, user_id: int):
        return self.message_repository.getMessages(user_id)

    def getMessage(self, message_id: int):
        return self.message_repository.getMessage(message_id)

    def createMessage(self, message: MessageSchema, current_usr):
        return self.message_repository.createMessage(message, current_usr)

    def getMessageCount(self, user_id: int):
        return self.message_repository.getMessageCount(user_id)

    def checkMessage(self, message_id: int, user_id: int):
        return self.message_repository.checkMessage(message_id, user_id)

    def deleteMessage(self, message_id: int):
        return self.message_repository.deleteMessage(message_id)