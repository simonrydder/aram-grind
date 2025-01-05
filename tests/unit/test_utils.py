from typing import Sequence

import pytest
from polars import List

from src.concrete.factories.alpha import Alpha
from src.concrete.standard_game import StandardGame
from src.interfaces.champion import Champion
from src.interfaces.factories.game import GameFactory
from src.interfaces.game import Game
from src.states.champion import ChampionState
from src.utils.dataframe import champion_to_dict, champions_to_dataframe


@pytest.fixture(scope="function")
def factory() -> GameFactory:
    return Alpha()


@pytest.fixture(scope="function")
def game(factory: GameFactory) -> Game:
    return StandardGame(factory)


@pytest.fixture(scope="function")
def champions(game: Game) -> Sequence[Champion]:
    return game.champions


def test_that_champions_to_dataframe_returns_dataframe_of_length_168(
    champions: Sequence[Champion],
) -> None:
    df = champions_to_dataframe(champions)

    assert len(df) == 168


def test_that_champions_dataframe_has_column_name(
    champions: Sequence[Champion],
) -> None:
    df = champions_to_dataframe(champions)

    assert "name" in df.columns


def test_that_champions_dataframe_does_not_have_image(
    champions: Sequence[Champion],
) -> None:
    df = champions_to_dataframe(champions)

    assert "image" not in df.columns


def test_that_champions_dataframe_has_tags(champions: Sequence[Champion]) -> None:
    df = champions_to_dataframe(champions)

    assert "tags" in df.columns


def test_that_champions_dataframe_tags_column_has_type_list_of_str(
    champions: Sequence[Champion],
) -> None:
    df = champions_to_dataframe(champions)

    assert isinstance(df.schema["tags"], List)


def test_that_champion_dict_has_same_keys_as_champion_state(
    champions: Sequence[Champion],
) -> None:
    champ = champions[0]

    dct = champion_to_dict(champ)

    state_fields = ChampionState.model_fields
    field_names = set(state_fields.keys())
    assert set(dct.keys()) == field_names
