import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean(), default=False, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    aws_credentials = relationship("AwsCredential")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)


    def __str__(self):
        return f"User ID: {self.id}"
