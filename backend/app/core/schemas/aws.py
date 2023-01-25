from pydantic import BaseModel, Field

from app.core.models.users import User

class AwsCredentialBase(BaseModel):
    name: str = Field(description="Name of project or credentials")


class AwsCredentialIn(AwsCredentialBase):
    access_key: str = Field(description="Aws Access key")
    secret_access_key: str = Field(description="Aws Secret Access Key")

class AwsCredentialOut(AwsCredentialBase):
    id: int
    
    class Config:
        orm_mode = True


class AwsCredentialInDB(AwsCredentialIn):
    pass
    # user: User
