from fastapi import APIRouter

router = APIRouter("/aws")


@router.get("/")
def index():
    return {"message": "Hello world"}
