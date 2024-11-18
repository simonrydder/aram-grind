from typing import Sequence

from pydantic import BaseModel

from src.states.champion import ChampionState
from src.states.player import PlayerState


class TeamState(BaseModel):
    players: Sequence[PlayerState]
    champions: Sequence[ChampionState]
    size: int
