import json
import os
from typing import Any, Iterator, Sequence

import pytest

from src.concrete.factories.alpha import Alpha
from src.concrete.factories.beta import Beta
from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.interfaces.game import Game
from src.interfaces.player import Player


@pytest.fixture(scope="function")
def players() -> Sequence[Player]:
    return [StandardPlayer(str(i + 1)) for i in range(6)]


@pytest.fixture(scope="function")
def alpha(players: Sequence[Player]) -> Game:
    game = StandardGame(Alpha())
    game.initialize_game(players)
    return game


@pytest.fixture(scope="function")
def save_file() -> Iterator[str]:
    file = "save_file"
    yield file

    saved_file = os.path.join("saves", f"{file}.json")
    os.remove(saved_file)


@pytest.fixture(scope="function")
def long_alpha(players: Sequence[Player]) -> Game:
    game = StandardGame(Alpha())
    game.initialize_game(players)

    game.new_round()
    game.update_winners(game.red)
    game.new_round()
    game.update_winners(game.red)
    game.new_round()
    game.update_winners(game.blue)

    return game


@pytest.fixture(scope="function")
def data(long_alpha: Game, save_file: str) -> Iterator[dict[str, Any]]:
    long_alpha.save_game(save_file)

    with open(save_file, "r") as f:
        yield json.load(f)


@pytest.fixture(scope="function")
def beta(players: Sequence[Player]) -> Game:
    game = StandardGame(Beta())
    game.initialize_game(players)
    return game
