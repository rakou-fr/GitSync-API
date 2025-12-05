from fastapi import APIRouter
from app.models.update_model import UpdateModel
from app.core.github import update_json

router = APIRouter()

@router.post("/update")
def update_route(body: UpdateModel):
    return update_json(body.data)
