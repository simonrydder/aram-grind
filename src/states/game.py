from typing import Sequence

from pydantic import BaseModel

from src.states.champion import ChampionState
from src.states.player import PlayerState


class GameState(BaseModel):
    players: Sequence[PlayerState]
    champions: Sequence[ChampionState]
