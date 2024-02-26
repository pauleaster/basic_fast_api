# schemas.py
from pydantic import ConfigDict, BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str

class Contact(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str
    submitted_at: datetime
    model_config = ConfigDict(from_attributes=True)
