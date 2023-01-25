from fastapi import Depends, HTTPException, status

from .auth import get_auth_user
from app.core.models.users import User

def get_active_user(user: User = Depends(get_auth_user)):
    if not user.active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="inactive_user")

    return user

def get_admin_user(user: User = Depends(get_active_user)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not_enough_permissions")

    return user
