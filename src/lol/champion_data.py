from pydantic import BaseModel


class ChampionData(BaseModel):
    id: str  # = Field(alias="id")
    name: str
    pass
