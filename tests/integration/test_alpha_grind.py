import json
import os
from typing import Any, Iterator, Sequence

import pytest

from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.concrete.strategies.player_assignment.first import (
    FirstPlayerAssignemntStrategy,
)
from src.interfaces.game import Game
from src.interfaces.player import Player


@pytest.fixture(scope="function")
def players() -> Sequence[Player]:
    return [StandardPlayer(str(i + 1)) for i in range(6)]


@pytest.fixture(scope="function")
def game(players: Sequence[Player]) -> Game:
    game = StandardGame(FirstPlayerAssignemntStrategy())
    game.initialize_game(players)
    return game


@pytest.fixture(scope="function")
def save_file() -> Iterator[str]:
    file = "save_file.json"
    yield file

    os.remove(file)


@pytest.fixture(scope="function")
def long_game(players: Sequence[Player]) -> Game:
    game = StandardGame(FirstPlayerAssignemntStrategy())
    game.initialize_game(players)

    game.new_round()
    game.update_winners(game.red)
    game.new_round()
    game.update_winners(game.red)
    game.new_round()
    game.update_winners(game.blue)

    return game


@pytest.fixture(scope="function")
def data(long_game: Game, save_file: str) -> Iterator[dict[str, Any]]:
    long_game.save_game(save_file)

    with open(save_file, "r") as f:
        yield json.load(f)


def test_that_game_has_6_players(game: Game):
    assert len(game.players) == 6


def test_that_player_2_has_name_2(game: Game):
    players = game.players
    player_2 = players[1]

    assert player_2.name == "2"


def test_that_red_team_has_size_3(game: Game):
    team = game.red

    assert team.size == 3


def test_that_red_team_has_size_2(players: Sequence[Player], game: Game):
    three_players = players[:3]
    game.initialize_game(three_players)
    team = game.red

    assert team.size == 2


def test_that_blue_team_has_size_3(game: Game):
    team = game.blue

    assert team.size == 3


def test_that_blue_team_has_size_1(players: Sequence[Player], game: Game):
    three_players = players[:3]
    game.initialize_game(three_players)
    team = game.blue

    assert team.size == 1


def test_that_168_unique_named_champions(game: Game):
    champions = game.champions
    unique_champions = {champ.name for champ in champions}

    assert len(unique_champions) == 168


def test_that_new_round_assign_3_players_to_red_team(game: Game):
    game.new_round()
    team = game.red

    assert len(team.players) == 3


def test_that_red_team_players_are_unique(game: Game):
    game.new_round()
    team = game.red

    unique_players = set(team.players)

    assert len(unique_players) == 3


def test_that_new_round_assign_3_players_to_blue_team(game: Game):
    game.new_round()
    team = game.blue

    assert len(team.players)


def test_that_blue_team_players_are_unique(game: Game):
    game.new_round()
    team = game.blue
    unique_players = set(team.players)

    assert len(unique_players) == 3


def test_that_players_are_different_on_the_two_teams(game: Game):
    game.new_round()
    red_players = game.red.players
    blue_players = game.blue.players

    assert set(red_players) != set(blue_players)


def test_that_new_round_assign_3_champions_to_red_team(game: Game):
    game.new_round()
    team = game.red

    assert len(team.champions)


def test_that_new_round_assign_3_champions_to_blue_team(game: Game):
    game.new_round()
    team = game.blue

    assert len(team.champions)


def test_that_red_team_champions_are_unique(game: Game):
    game.new_round()
    team = game.red
    unique_champions = set(team.champions)

    assert len(unique_champions) == 3


def test_that_blue_team_champions_are_unique(game: Game):
    game.new_round()
    team = game.blue
    unique_champions = set(team.champions)

    assert len(unique_champions) == 3


def test_that_champions_are_different_on_the_two_teams(game: Game):
    game.new_round()
    red_champions = game.red.champions
    blue_champions = game.blue.champions

    assert set(red_champions) != set(blue_champions)


def test_that_players_on_winning_team_has_1_point(game: Game):
    game.new_round()
    players = game.red.players
    game.update_winners(game.red)

    for player in players:
        assert player.score == 1


def test_that_update_winner_resets_red_team(game: Game):
    game.new_round()
    game.update_winners(game.red)
    team = game.red

    assert len(team.players) == 0


def test_that_update_winner_resets_blue_team(game: Game):
    game.new_round()
    game.update_winners(game.red)
    team = game.blue

    assert len(team.players) == 0


def test_that_players_has_two_points_after_two_wins(game: Game):
    game.new_round()
    game.update_winners(game.red)

    game.new_round()
    players = game.red.players
    game.update_winners(game.red)

    for player in players:
        assert player.score == 2


def test_that_player_2_is_on_second_place(game: Game):
    game.new_round()
    score_board = game.get_scoreboard()
    first = score_board[1]

    assert first.name == "2"


def test_that_player_5_is_on_second_place(game: Game):
    game.new_round()
    game.update_winners(game.blue)
    score_board = game.get_scoreboard()
    first = score_board[1]

    assert first.name == "5"


def test_that_player_4_is_winning(game: Game):
    game.new_round()
    game.update_winners(game.blue)

    winner = game.get_winner()

    assert winner.name == "4"


def test_that_played_champions_become_disabled(game: Game):
    game.new_round()
    red_champions = game.red.champions
    blue_champions = game.blue.champions

    game.update_winners(game.red)

    for champion in red_champions:
        assert not champion.available

    for champion in blue_champions:
        assert not champion.available


def test_that_champions_in_second_round_is_new(game: Game):
    game.new_round()
    played_champions = set(game.red.champions) | set(game.blue.champions)
    game.update_winners(game.red)
    game.new_round()

    new_champions = list(game.red.champions) + list(game.blue.champions)
    for new_champ in new_champions:
        assert new_champ not in played_champions


def test_that_save_game_create_saved_file(long_game: Game, save_file: str):
    long_game.save_game(save_file)

    assert os.path.exists(save_file)


def test_that_loaded_game_has_player_1_with_score_2(
    game: Game, long_game: Game, save_file: str
):
    long_game.save_game(save_file)
    game.load_game(save_file)

    player = game.players[0]

    assert player.score == 2


def test_that_loaded_game_has_first_able_champion_(
    game: Game, long_game: Game, save_file: str
):
    long_game.save_game(save_file)
    game.load_game(save_file)

    for champ in game.champions:
        if champ.available:
            assert champ.name == "Briar"
            break
