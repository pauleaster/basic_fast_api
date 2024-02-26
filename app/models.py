# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from sqlalchemy.sql import func

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), index=True)
    phone = Column(String(20), index=True)
    message = Column(Text)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
