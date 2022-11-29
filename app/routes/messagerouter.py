from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.token import Token
from app.database.models.Users import User
from app.database.models.Messages import Messages
from app.service.service_messages import ServiceMessage

router = APIRouter(prefix="/message", tags=["Message"])

@router.get("/getMessages/{user_id}")
def getMessages(user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceMessage(db)
        messages = service.getMessages(user_id)
        return messages
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.post("/createMessage/{user_id}")
def createMessage(user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser),  message: Messages = Depends()):
    try:
        service = ServiceMessage(db)
        return service.createMessage(user_id, message, current_usr)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )

@router.get("/getMessage/{message_id}")
def getMessage(message_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceMessage(db)
        message = service.getMessage(message_id)
        return message
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.get("/getMessageCount/{user_id}")
def getMessageCount(user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceMessage(db)
        return service.getMessageCount(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.get("/checkMessage/{message_id}/{user_id}")
def checkMessage(message_id: int, user_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceMessage(db)
        return service.checkMessage(message_id, user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


@router.delete("/deleteMessage/{message_id}")
def deleteMessage(message_id: int, db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceMessage(db)
        return service.deleteMessage(message_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )