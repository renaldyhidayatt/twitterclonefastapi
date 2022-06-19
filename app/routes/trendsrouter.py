from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.database.models.Tweet import Tweet
from app.database.models.Users import User
from app.database.models.Trends import Trends
from app.schema.trends import TrendCreateSchema, TrendsResponseSchema
from app.core.token import Token
from app.service.service_trend import ServiceTrends

router = APIRouter(prefix="/trends", tags=["Trends"])

@router.get("/", response_model=List[TrendsResponseSchema])
def trends(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:

        service = ServiceTrends(db)
        return service.trends()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
        )


@router.post("/create")
def create(trend: TrendCreateSchema, current_usr: str = Depends(Token.get_currentUser),db: Session = Depends(get_db)):
    try:
        service = ServiceTrends(db)
        return service.create(trend, current_usr)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
        )


@router.get("/count")
def count(db: Session = Depends(get_db), current_usr: str = Depends(Token.get_currentUser)):
    try:
        service = ServiceTrends(db)
        return service.countTrends()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid {e}"
        )


