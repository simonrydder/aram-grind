from pydantic import BaseModel


class ChampionState(BaseModel):
    name: str
    available: bool
