from typing import Sequence

import pytest

from src.concrete.factories.alpha import Alpha
from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.concrete.strategies.champion_assignment.balanced import (
    BalancedChampionAssignment,
)
from src.concrete.strategies.champion_assignment.tag_based import (
    TagBasedChampionAssignment,
)
from src.interfaces.factories.game import GameFactory
from src.interfaces.game import Game
from src.interfaces.player import Player
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy


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
def tag() -> ChampionAssignmentStrategy:
    return TagBasedChampionAssignment()


@pytest.fixture(scope="function")
def balanced() -> ChampionAssignmentStrategy:
    return BalancedChampionAssignment()


def test_tag_based_strategy(tag: ChampionAssignmentStrategy, game: Game) -> None:
    tag.apply(game)


def test_balanced_strategy(balanced: ChampionAssignmentStrategy, game: Game) -> None:
    balanced.apply(game)


# TODO: Change it such that there is a champ selector strategy and a champ assigner strategy
