from typing import Any

import requests

from src.lol.champion_data import ChampionData


def fetch_versions(url: str) -> list[str]:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_latest_version(versions: list[str]) -> str:
    return versions[0]


def get_data_url(version: str, language: str) -> str:
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json"
    return url


def get_champion_data(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def convert_champion_data(data: dict[str, Any]) -> list[ChampionData]:

    champion_data: dict = data.get("data", {})

    return [ChampionData(**data) for data in champion_data.values()]


if __name__ == "__main__":
    from .language import Language

    versions = fetch_versions("https://ddragon.leagueoflegends.com/api/versions.json")
    print(versions)

    version = get_latest_version(versions)
    data_url = get_data_url(version, Language.US)
    data = get_champion_data(data_url)
    print(data)

    pass
