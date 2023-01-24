from sqlalchemy.orm import Session
from app.core.schemas.users import UserCreate
from app.core.models.users import User

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter_by(username=username).first()

def create_user(db: Session, user: UserCreate, **kwargs) -> User:
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    user = User(**user.dict(), **kwargs)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session, **kwargs) -> list[User]:
    return db.query(User).filter_by(**kwargs).all()


def get_user_by_id(db: Session, id: int) -> User:
    return db.query(User).filter_by(id=id).first()
