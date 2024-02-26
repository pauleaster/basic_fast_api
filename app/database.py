# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


testing = os.getenv("TESTING", "False").lower() == "true"

# Load environment files from .env file
if testing:
    print("************************ Loading testing database ************************")
    load_dotenv(".env.test", override=True)
else:
    print("************************ Loading development database ********************")
    load_dotenv(".env", override=True)

# Replace the following URL with your actual database connection string
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# An Engine, which the Session will use for connection resources
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your models
Base = declarative_base()
