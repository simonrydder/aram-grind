from typing import Sequence

from pydantic import BaseModel

from api.data.champion import ChampionData
from api.data.player import PlayerData


class TeamData(BaseModel):
    players: Sequence[PlayerData]
    champions: Sequence[ChampionData]
