from sqlalchemy.orm import Session

from app.core.models.users import User
from app.core.models.aws import AwsCredential
from app.core.schemas.aws import AwsCredentialInDB

def create_credential(db: Session, credentials: AwsCredentialInDB, user: User) -> AwsCredential:
   
    credentials = AwsCredential(**credentials.dict(), user=user)

    db.add(credentials)
    db.commit()
    db.refresh(credentials)

    return credentials
