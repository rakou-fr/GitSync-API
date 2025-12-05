from pydantic import BaseModel

class UpdateModel(BaseModel):
    data: dict
