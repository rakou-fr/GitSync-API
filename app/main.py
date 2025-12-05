from fastapi import FastAPI
from app.routes import read, update

app = FastAPI()

app.include_router(read.router)
app.include_router(update.router)
