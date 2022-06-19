from fastapi import HTTPException, status, Response
from app.database.models.Messages import Messages
from app.database.models.Users import User
from ..schema.messages import MessageSchema

class RepoMessage:
    def __init__(self, session) -> None:
        self.session = session

    def getMessages(self,user_id: int):
        messages = self.session.query(Messages).filter(Messages.user_id == user_id).all()
        return messages

    def getMessage(self,message_id: int):
        message = self.db.query(Messages).filter(Messages.id == message_id).first()
        if not message:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

        return message

    def createMessage(self,message: MessageSchema, current_usr):
        user = self.query(User).filter(User.username == current_usr).first()
        message = Messages(messageBy=user.id, messageTo=message.messageTo, message=message.message)
        self.db.add(message)
        self.db.commit()

        return message

    def getMessageCount(self,user_id: int):
        messages = self.db.query(Messages).filter(Messages.user_id == user_id).count()
        return messages

    def checkMessage(self,message_id: int, user_id: int):
        messages = self.db.query(Messages).filter(Messages.id == message_id).filter(Messages.user_id == user_id).first()
        if not messages:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

        return messages
    
    def deleteMessage(self,message_id):
        message = self.db.query(Messages).filter(Messages.id == message_id).first()
        if not message:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

        self.db.delete(message)
        self.db.commit()
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
