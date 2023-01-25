from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, ExpiredSignatureError
from sqlalchemy.orm import Session

from app.core.repositories.users import get_user_by_id
from app.core.services.auth import auth_service
from app.core.schemas.jwt import TokenData
from app.dependencies.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_auth_user(*,
                  token: str = Depends(oauth2_scheme),
                  db: Session = Depends(get_db),
                  request: Request):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid_credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    credentials_expired = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token_expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        decoded_token = auth_service.decode_access_token(token)

        id = decoded_token.get("sub")
        if not id:
            raise credentials_exception

        data = TokenData(id=id)
    except ExpiredSignatureError:
        raise credentials_expired
    except JWTError:
        raise credentials_exception

    user = get_user_by_id(db, id)

    if not user:
        raise credentials_exception
    # save for further usage
    request.state.user = user
    return user
