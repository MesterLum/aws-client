from pydantic import BaseModel, Field

class MessageBase(BaseModel):
    detail: str = Field(title="Detail", description="Describes the reason of the error")
