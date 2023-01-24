from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from app.core.schemas.jwt import Token
from app.core.schemas.common import MessageBase

from app.core.services.auth import auth_service

from app.dependencies.database import get_db

router = APIRouter(
        prefix="/auth",
        tags=["auth"]

    )


@router.post("/login", response_model=Token, responses={404: {"model": MessageBase}})
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User or password incorrect")

    return auth_service.create_access_token_and_refresh_token(user.id)
