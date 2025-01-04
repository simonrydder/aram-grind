from typing import Set

from pydantic import BaseModel


class ChampionState(BaseModel):
    name: str
    available: bool
    image: str | None = None
    loading: str | None = None
    tags: Set[str] | None = None
    physical: int | None = None
