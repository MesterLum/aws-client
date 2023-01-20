from fastapi import FastAPI

from app.config import settings

app = FastAPI(debug=settings.debug, title="S3 Client")
