from fastapi import FastAPI
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from .database import create_db_and_tables, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creatitng tables.. lifespan start")
    create_db_and_tables()
    yield
    print("lifespan end")

app: FastAPI = FastAPI(
    lifespan=lifespan,
    title="first Fast Api application",
    description="this is frist small api created with FastApi",
)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/health")
def health():
    return {"status": "ok"}