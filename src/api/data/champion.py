from pydantic import BaseModel


class ChampionData(BaseModel):
    name: str
