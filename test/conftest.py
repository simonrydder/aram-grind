from collections.abc import Iterator

import pytest

from src.concrete.standard_champion import StandardChampion
from src.utils.lol import ChampionDragon, Language, get_champion_data, get_data_url


@pytest.fixture(scope="module")
def patch() -> Iterator[str]:
    yield "14.19.1"


@pytest.fixture(scope="module")
def language() -> Iterator[str]:
    yield Language.US


@pytest.fixture(scope="module")
def champion_data(patch: str, language: str) -> Iterator[dict[str, ChampionDragon]]:
    url = get_data_url(patch, language)
    data = get_champion_data(url)

    yield data.data


@pytest.fixture(scope="function")
def aatrox_data(champion_data: dict[str, ChampionDragon]) -> Iterator[ChampionDragon]:
    yield champion_data["Aatrox"]


@pytest.fixture(scope="function")
def aatrox(aatrox_data: ChampionDragon) -> Iterator[StandardChampion]:
    yield StandardChampion(aatrox_data)


@pytest.fixture(scope="function")
def ekko_data(champion_data: dict[str, ChampionDragon]) -> Iterator[ChampionDragon]:
    yield champion_data["Ekko"]


@pytest.fixture(scope="function")
def ekko(ekko_data: ChampionDragon) -> Iterator[StandardChampion]:
    yield StandardChampion(ekko_data)
