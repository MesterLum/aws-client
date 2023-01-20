import datetime

from app.database import Base
from sqlalchemy import (
        Column,
        Integer,
        String,
        Boolean,
        DateTime,
        ForeignKey
)

class AwsCredential(Base):

    __tablename__ = "aws_credentials"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    access_key = Column(String(255), nullable=False)
    secret_access_key = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)


    

    def __str__(self):
        return self.id
