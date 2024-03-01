# app/main.py
import warnings
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/django/api/contacts/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    print("Creating contact")
    print(f"Contact = \n{contact}\n")
    return crud.create_contact(db=db, contact=contact)

@app.get("/django/api/contacts/{contact_id}", response_model=schemas.Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    print(f"Reading contact with id = {contact_id}")
    db_contact = crud.get_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.delete("/django/api/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    if not crud.delete_contact(db=db, contact_id=contact_id):
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}