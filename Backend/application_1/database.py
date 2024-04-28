from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv
load_dotenv()

connection_string = os.getenv('DATABASE_URL')
if connection_string is None:
    raise ValueError("DATABASE_URL environment variable is not set")
engine = create_engine(connection_string, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)