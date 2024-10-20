from enum import StrEnum

import requests
from pydantic import BaseModel


class Language(StrEnum):
    US = "en_US"
    FR = "fr_FR"


class InfoData(BaseModel):
    attack: int
    defense: int
    magic: int
    difficulty: int


class ImageData(BaseModel):
    full: str
    sprite: str
    group: str
    x: int
    y: int
    w: int
    h: int


class StatsData(BaseModel):
    hp: float
    hpperlevel: float
    mp: float
    mpperlevel: float
    movespeed: float
    armor: float
    armorperlevel: float
    spellblock: float
    spellblockperlevel: float
    attackrange: float
    hpregen: float
    hpregenperlevel: float
    mpregen: float
    mpregenperlevel: float
    crit: float
    critperlevel: float
    attackdamage: float
    attackdamageperlevel: float
    attackspeedperlevel: float
    attackspeed: float


class ChampionData(BaseModel):
    version: str
    id: str
    key: int
    name: str
    title: str
    blurb: str
    info: InfoData
    image: ImageData
    tags: list[str]
    partype: str
    stats: StatsData


class LolDataDragon(BaseModel):
    type: str
    format: str
    version: str
    data: dict[str, ChampionData]


def fetch_versions() -> list[str]:
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_latest_version(versions: list[str]) -> str:
    return versions[0]


def get_data_url(version: str, language: str) -> str:
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json"
    return url


def get_champion_data(url: str) -> LolDataDragon:
    response = requests.get(url)
    response.raise_for_status()
    res = response.json()
    dd = LolDataDragon(**res)
    return dd


if __name__ == "__main__":
    url = get_data_url("14.19.1", Language.US)
    get_champion_data(url)
#     from .language import Language

#     versions = fetch_versions("https://ddragon.leagueoflegends.com/api/versions.json")
#     print(versions)

#     version = get_latest_version(versions)
#     data_url = get_data_url(version, Language.US)
#     data = get_champion_data(data_url)
#     print(data)

#     pass
