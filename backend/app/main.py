from fastapi import FastAPI
from app.config import settings
from app.v1 import router as v1_router

app = FastAPI(debug=settings.debug, title="S3 Client")


app.include_router(v1_router)

@app.get("/ping")
async def ping():
    return {"msg": "Pong"}
