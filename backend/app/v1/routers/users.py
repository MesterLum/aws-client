from fastapi import APIRouter, Depends, HTTPException, status, Path, Request
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.core.repositories.users import create_user as create_user_in_db, get_user_by_username, get_users, get_user_by_id
from app.core.schemas.users import UserCreate, UserCreateOut, UserDetailOut, UserDetailIn
from app.core.schemas.common import MessageBase
from app.dependencies.users import get_admin_user
from app.core.models.users import User

router = APIRouter(
            prefix="/users",
            tags=["users"],
            dependencies=[Depends(get_admin_user)]
        )


@router.post("/", status_code=201, response_model=UserCreateOut, responses={
        302: {"model": MessageBase}
})
async def create_user(user: UserCreate, db: Session = Depends(get_db)):

    user_exists = get_user_by_username(db, user.username)
    
    if user_exists:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Username already exists")

    user = create_user_in_db(db, user)

    return user

@router.get("/", response_model=list[UserDetailOut])
async def list_users(db: Session = Depends(get_db)):
    users = get_users(db)

    return users

@router.put("/{id}", response_model=UserDetailOut)
async def update_user(*,
                    user: UserDetailIn,
                    id: int = Path(title="User ID"),
                    db: Session = Depends(get_db) 
                ):
    user_in_db = get_user_by_id(db, id) 

    if not user_in_db:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user_dict = user.dict()
    for key in user.dict():
       setattr(user_in_db, key, user_dict[key])

    db.commit()
    return user_in_db

@router.get("/me")
async def read_me():
    return {"message": "WOlrd"}
