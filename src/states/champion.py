from typing import Sequence

from pydantic import BaseModel


class ChampionState(BaseModel):
    name: str
    available: bool
    image: str | None = None
    loading: str | None = None
    tags: Sequence[str] | None = None
    physical: int | None = None
    defense: int | None = None
    magic: int | None = None
    difficulty: int | None = None
