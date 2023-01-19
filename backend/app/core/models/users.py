from sqlalchemy import (
    Column,
    Integer,
    String,
)
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


    def __str__(self):
        return f"User ID: {self.id}"
