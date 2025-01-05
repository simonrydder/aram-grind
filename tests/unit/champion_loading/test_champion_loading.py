from typing import Sequence

import pytest

from src.concrete.factories.alpha import Alpha
from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.concrete.strategies.champion_loading.fixed import (
    FixedChampionLoadingStrategy,
)
from src.concrete.strategies.champion_loading.latest import (
    LatestChampionLoadingStrategy,
)
from src.interfaces.factories.game import GameFactory
from src.interfaces.game import Game
from src.interfaces.player import Player
from src.interfaces.strategies.champion_loading import ChampionLoadingStrategy


@pytest.fixture(scope="function")
def factory() -> GameFactory:
    return Alpha()


@pytest.fixture(scope="function")
def players() -> Sequence[Player]:
    return [StandardPlayer(str(i + 1)) for i in range(6)]


@pytest.fixture(scope="function")
def game(factory: GameFactory, players: Sequence[Player]) -> Game:
    game = StandardGame(factory)
    game.initialize_game(players=players)
    return game


@pytest.fixture(scope="function")
def fixed() -> ChampionLoadingStrategy:
    return FixedChampionLoadingStrategy()


@pytest.fixture(scope="function")
def fixed_14_24() -> ChampionLoadingStrategy:
    return FixedChampionLoadingStrategy("14.24.1")


def test_that_fixed_14_19_1_does_not_have_ambessa(game: Game):
    loading = FixedChampionLoadingStrategy("14.19.1")
    champions = loading.load(game)

    assert "Ambessa" not in [c.name for c in champions]


def test_that_fixed_14_24_1_does_have_ambessa(game: Game):
    loading = FixedChampionLoadingStrategy("14.24.1")
    champions = loading.load(game)

    assert "Ambessa" in [c.name for c in champions]


def test_that_last_does_have_ambessa(game: Game):
    loading = LatestChampionLoadingStrategy()
    champions = loading.load(game)

    assert "Ambessa" in [c.name for c in champions]
