from fastapi import APIRouter
from app.core.github import read_json

router = APIRouter()

@router.get("/read")
def read_route():
    return read_json()
