from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str = Field(title="Username unique", min_length=3, max_length=50, description="A unique username")

class UserCreate(UserBase):
    password: str = Field(title="Password 1", min_length=8, max_length=255, description="Password 1")

class UserCreateOut(UserBase):
    id: int

    class Config:
        orm_mode = True
