import pytest

from src.concrete.factories.alpha import Alpha
from src.concrete.standard_game import StandardGame
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


def test_that_champions_to_dataframe_returns_dataframe_of_length_168(
    game: Game,
) -> None:
    champions = game.champions

    df = champions_to_dataframe(champions)

    assert len(df) == 168


def test_that_champion_dict_has_same_keys_as_champion_state(game: Game) -> None:
    champions = game.champions
    champ = champions[0]

    dct = champion_to_dict(champ)

    state_fields = ChampionState.model_fields
    field_names = set(state_fields.keys())
    assert set(dct.keys()) == field_names


def test_that_champions_dataframe_has_column_name(game: Game) -> None:
    champions = game.champions

    df = champions_to_dataframe(champions)

    assert "name" in df.columns
