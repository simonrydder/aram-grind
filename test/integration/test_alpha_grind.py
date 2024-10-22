from typing import Iterator, Sequence

import pytest

from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.interfaces.game import Game
from src.interfaces.player import Player


@pytest.fixture(scope="function")
def players() -> Iterator[Sequence[Player]]:

    yield [StandardPlayer(str(i + 1)) for i in range(6)]


@pytest.fixture(scope="function")
def game(players) -> Iterator[Game]:
    yield StandardGame(players)


def test_that_game_has_6_players(game: Game):
    assert len(game.players) == 6


def test_that_player_2_has_name_2(game: Game):
    players = game.players
    player_2 = players[1]

    assert player_2.name == "2"


def test_that_red_team_has_size_3(game: Game):
    team = game.red

    assert team.size == 3


def test_that_red_team_has_size_2(players: Sequence[Player]):
    three_players = players[:3]
    game = StandardGame(three_players)
    team = game.red

    assert team.size == 2


def test_that_blue_team_has_size_3(game: Game):
    team = game.blue

    assert team.size == 3


def test_that_blue_team_has_size_1(players: Sequence[Player]):
    three_players = players[:3]
    game = StandardGame(three_players)
    team = game.blue

    assert team.size == 1


def test_that_168_unique_named_champions(game: Game):
    champions = game.champions

    unique_champions = {champ.name for champ in champions}
    assert len(unique_champions) == 168
