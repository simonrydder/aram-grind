from collections.abc import Iterator
from typing import Callable

import pytest

from src.concrete.standard_champion import StandardChampion
from src.interfaces.champion import Champion
from src.utils.lol import ChampionData, Language, get_champion_data, get_data_url


@pytest.fixture(scope="module")
def patch() -> Iterator[str]:
    yield "14.19.1"


@pytest.fixture(scope="module")
def language() -> Iterator[str]:
    yield Language.US


@pytest.fixture(scope="module")
def champion_data(patch: str, language: str) -> Iterator[dict[str, ChampionData]]:
    url = get_data_url(patch, language)
    data = get_champion_data(url)

    yield data.data


@pytest.fixture(scope="function")
def champ_int(champion_data: dict[str, ChampionData]) -> Callable[[int], Champion]:
    def _create_ith_champion(number: int) -> Champion:
        data = list(champion_data.values())[number]
        return StandardChampion(data)

    return _create_ith_champion


@pytest.fixture(scope="function")
def champ_name(champion_data: dict[str, ChampionData]) -> Callable[[str], Champion]:
    def _create_champion(name: str) -> Champion:
        data = champion_data.get(name)
        assert isinstance(data, ChampionData)

        return StandardChampion(data)

    return _create_champion
