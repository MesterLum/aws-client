from fastapi import APIRouter

router = APIRouter(
        prefix="/aws",
        tags=["aws"]
        )


@router.get("/")
def index():
    return {"message": "Hello world"}
