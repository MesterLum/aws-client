from fastapi import APIRouter

from .routers.aws import router as aws_router
from .routers.users import router as user_router

router = APIRouter(prefix="/api/v1")

router.include_router(aws_router)
router.include_router(user_router)
