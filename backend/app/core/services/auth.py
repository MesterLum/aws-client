import datetime

from dataclasses import dataclass

from app.config import settings
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.core.models.users import User
from app.core.repositories.users import get_user_by_username
from app.core.schemas.jwt import Token

SECRET_KEY = settings.secret_key
SECRET_KEY_REFRESH = settings.secret_key_refresh
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 60 * 7


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@dataclass(order=True, frozen=True)
class AuthService:
    secret_key: str
    secret_key_refresh: str
    algorithm: str
    access_token_expiration: int
    refresh_token_expires: int


    def __verify_password(self, plain_password, hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def __hash_password(self, plain_password) -> str:
        return pwd_context.hash(plain_password)

    def authenticate_user(self, db: Session, username: str, password: str):
        user = get_user_by_username(db, username)

        if not user:
            return False

        if not self.__verify_password(password, user.password):
            return False

        return user


    def create_access_token_and_refresh_token(self, id: int) -> Token:

        access_token_expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=self.access_token_expiration)
        refresh_token_expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=self.refresh_token_expires)

        encoded_access_token = jwt.encode({"sub": str(id), "exp": access_token_expires}, self.secret_key, algorithm=self.algorithm)
        encoded_refresh_token = jwt.encode({"sub": str(id), "exp": refresh_token_expires}, self.secret_key_refresh, algorithm=self.algorithm)

        return Token(access_token=encoded_access_token, refresh_token=encoded_refresh_token, token_type="bearer") 

    def decode_access_token(self, token: str):
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])


        

auth_service = AuthService(SECRET_KEY, SECRET_KEY_REFRESH,
                           ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES,
                           REFRESH_TOKEN_EXPIRE_MINUTES)
