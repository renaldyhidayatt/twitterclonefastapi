from ..repository.repo_message import RepoMessage
from ..schema.messages import MessageSchema

class ServiceMessage(RepoMessage):
    def __init__(self, session) -> None:
        super().__init__(session)
        
    def getMessages(self, user_id: int):
        return super().getMessages(user_id)

    def getMessage(self, message_id: int):
        return super().getMessage(message_id)

    def createMessage(self, message: MessageSchema, current_usr):
        return super().createMessage(message, current_usr)

    def getMessageCount(self, user_id: int):
        return super().getMessageCount(user_id)

    def checkMessage(self, message_id: int, user_id: int):
        return super().checkMessage(message_id, user_id)

    def deleteMessage(self, message_id: int):
        return super().deleteMessage(message_id)