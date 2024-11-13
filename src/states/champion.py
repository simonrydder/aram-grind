from pydantic import BaseModel


class ChampionState(BaseModel):
    name: str
    available: bool
    image: str | None = None
    loading: str | None = None
