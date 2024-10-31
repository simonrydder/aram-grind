from pydantic import BaseModel


class PlayerData(BaseModel):
    name: str
    score: int
