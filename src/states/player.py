from pydantic import BaseModel


class PlayerState(BaseModel):
    name: str
    score: int
