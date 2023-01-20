from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.core.repositories.users import create_user as create_user_in_db, get_user_by_username
from app.core.schemas.users import UserCreate, UserCreateOut

router = APIRouter(
            prefix="/users",
            tags=["users"]
        )


@router.post("/", status_code=201, responses={
    201: {"model": UserCreateOut}
    })
async def create_user(user: UserCreate, db: Session = Depends(get_db)):

    user_exists = get_user_by_username(db, user.username)
    
    if user_exists:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Username already exists")

    user = create_user_in_db(db, user)

    return user

