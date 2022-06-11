from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.utils.token import Token
from app.database.models.Users import User
from app.database.models.Messages import Messages

router = APIRouter(prefix="/message", tags=["Message"])

@router.get("/getMessages/{user_id}")
def getMessages(user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    messages = db.query(Messages).filter(Messages.user_id == user_id).all()
    return messages


@router.post("/createMessage/{user_id}")
def createMessage(user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser),  message: Messages = Depends()):
    user = db.query(User).filter(User.id == current_usr).first()
    message = Messages(messageBy=user.id, messageFrom=user_id, message=message.message)
    db.add(message)
    db.commit()

    return message

@router.get("/getMessage/{message_id}")
def getMessage(message_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    message = db.query(Messages).filter(Messages.id == message_id).first()
    if not message:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

    return message


@router.get("/getMessageCount/{user_id}")
def getMessageCount(user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    messages = db.query(Messages).filter(Messages.user_id == user_id).count()
    return messages


@router.get("/checkMessage/{message_id}/{user_id}")
def checkMessage(message_id: int, user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    messages = db.query(Messages).filter(Messages.id == message_id).filter(Messages.user_id == user_id).first()
    if not messages:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

    return messages


@router.delete("/deleteMessage/{message_id}")
def deleteMessage(message_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    message = db.query(Messages).filter(Messages.id == message_id).first()
    if not message:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

    db.delete(message)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)