from enum import StrEnum

import requests
from pydantic import BaseModel

BASE_URL = "https://ddragon.leagueoflegends.com/"


class Language(StrEnum):
    US = "en_US"
    FR = "fr_FR"


class InfoDragon(BaseModel):
    attack: int
    defense: int
    magic: int
    difficulty: int


class ImageDragon(BaseModel):
    full: str
    sprite: str
    group: str
    x: int
    y: int
    w: int
    h: int


class StatsDragon(BaseModel):
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


class ChampionDragon(BaseModel):
    version: str
    id: str
    key: int
    name: str
    title: str
    blurb: str
    info: InfoDragon
    image: ImageDragon
    tags: list[str]
    partype: str
    stats: StatsDragon


class LolDataDragon(BaseModel):
    type: str
    format: str
    version: str
    data: dict[str, ChampionDragon]


def fetch_versions() -> list[str]:
    url = f"{BASE_URL}api/versions.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_latest_version(versions: list[str]) -> str:
    return versions[0]


def get_data_url(version: str, language: str) -> str:
    url = f"{BASE_URL}cdn/{version}/data/{language}/champion.json"
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
