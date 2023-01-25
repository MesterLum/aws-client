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
from sqlalchemy.orm import relationship

class AwsCredential(Base):

    __tablename__ = "aws_credentials"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    access_key = Column(String(255), nullable=False)
    secret_access_key = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    user = relationship("User", back_populates="aws_credentials")

    def __str__(self):
        return self.id
