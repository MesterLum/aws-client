from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Request

from app.dependencies.users import get_active_user
from app.core.schemas.common import MessageBase
from app.core.schemas.aws import AwsCredentialIn, AwsCredentialOut, AwsCredentialInDB
from app.core.repositories.aws import create_credential
from app.dependencies.database import get_db

router = APIRouter(
        prefix="/aws",
        tags=["Aws credentials"],
        dependencies=[Depends(get_active_user)],
        responses={
            401: {"model": MessageBase}
        }
    )


@router.get("/", response_model=list[AwsCredentialOut])
def list_credentials(request: Request):
    user = request.state.user

    return user.aws_credentials


@router.post("/", response_model=AwsCredentialOut, status_code=status.HTTP_201_CREATED)
def register_aws_credentials(*,
                            db: Session = Depends(get_db),
                            aws_credential: AwsCredentialIn,
                            request: Request):

    user = request.state.user

    credentials = create_credential(db, aws_credential, user)
    return credentials

# @router.put("/{credential_id}")
# def update_credentials(*,
                       # db: Session = Depends(get_db),
                       # request: Request):
