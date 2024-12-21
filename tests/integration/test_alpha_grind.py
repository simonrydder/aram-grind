import os
from typing import Sequence

from src.interfaces.game import Game
from src.interfaces.player import Player


def test_that_game_has_6_players(alpha: Game):
    assert len(alpha.players) == 6


def test_that_player_2_has_name_2(alpha: Game):
    players = alpha.players
    player_2 = players[1]

    assert player_2.name == "2"


def test_that_red_team_has_size_3(alpha: Game):
    team = alpha.red

    assert team.size == 3


def test_that_red_team_has_size_2(players: Sequence[Player], alpha: Game):
    three_players = players[:3]
    alpha.initialize_game(three_players)
    team = alpha.red

    assert team.size == 2


def test_that_blue_team_has_size_3(alpha: Game):
    team = alpha.blue

    assert team.size == 3


def test_that_blue_team_has_size_1(players: Sequence[Player], alpha: Game):
    three_players = players[:3]
    alpha.initialize_game(three_players)
    team = alpha.blue

    assert team.size == 1


def test_that_168_unique_named_champions(alpha: Game):
    champions = alpha.champions
    unique_champions = {champ.name for champ in champions}

    assert len(unique_champions) == 168


def test_that_new_round_assign_3_players_to_red_team(alpha: Game):
    alpha.new_round()
    team = alpha.red

    assert len(team.players) == 3


def test_that_red_team_players_are_unique(alpha: Game):
    alpha.new_round()
    team = alpha.red

    unique_players = set(team.players)

    assert len(unique_players) == 3


def test_that_new_round_assign_3_players_to_blue_team(alpha: Game):
    alpha.new_round()
    team = alpha.blue

    assert len(team.players)


def test_that_blue_team_players_are_unique(alpha: Game):
    alpha.new_round()
    team = alpha.blue
    unique_players = set(team.players)

    assert len(unique_players) == 3


def test_that_players_are_different_on_the_two_teams(alpha: Game):
    alpha.new_round()
    red_players = alpha.red.players
    blue_players = alpha.blue.players

    assert set(red_players) != set(blue_players)


def test_that_new_round_assign_3_champions_to_red_team(alpha: Game):
    alpha.new_round()
    team = alpha.red

    assert len(team.champions)


def test_that_new_round_assign_3_champions_to_blue_team(alpha: Game):
    alpha.new_round()
    team = alpha.blue

    assert len(team.champions)


def test_that_red_team_champions_are_unique(alpha: Game):
    alpha.new_round()
    team = alpha.red
    unique_champions = set(team.champions)

    assert len(unique_champions) == 3


def test_that_blue_team_champions_are_unique(alpha: Game):
    alpha.new_round()
    team = alpha.blue
    unique_champions = set(team.champions)

    assert len(unique_champions) == 3


def test_that_champions_are_different_on_the_two_teams(alpha: Game):
    alpha.new_round()
    red_champions = alpha.red.champions
    blue_champions = alpha.blue.champions

    assert set(red_champions) != set(blue_champions)


def test_that_players_on_winning_team_has_1_point(alpha: Game):
    alpha.new_round()
    players = alpha.red.players
    alpha.update_winners(alpha.red)

    for player in players:
        assert player.score == 1


def test_that_update_winner_resets_red_team(alpha: Game):
    alpha.new_round()
    alpha.update_winners(alpha.red)
    team = alpha.red

    assert len(team.players) == 0


def test_that_update_winner_resets_blue_team(alpha: Game):
    alpha.new_round()
    alpha.update_winners(alpha.red)
    team = alpha.blue

    assert len(team.players) == 0


def test_that_players_has_two_points_after_two_wins(alpha: Game):
    alpha.new_round()
    alpha.update_winners(alpha.red)

    alpha.new_round()
    players = alpha.red.players
    alpha.update_winners(alpha.red)

    for player in players:
        assert player.score == 2


def test_that_player_2_is_on_second_place(alpha: Game):
    alpha.new_round()
    score_board = alpha.get_scoreboard()
    first = score_board[1]

    assert first.name == "2"


def test_that_player_5_is_on_second_place(alpha: Game):
    alpha.new_round()
    alpha.update_winners(alpha.blue)
    score_board = alpha.get_scoreboard()
    first = score_board[1]

    assert first.name == "5"


def test_that_player_4_is_winning(alpha: Game):
    alpha.new_round()
    alpha.update_winners(alpha.blue)

    winner = alpha.get_winner()

    assert winner.name == "4"


def test_that_played_champions_become_disabled(alpha: Game):
    alpha.new_round()
    red_champions = alpha.red.champions
    blue_champions = alpha.blue.champions

    alpha.update_winners(alpha.red)

    for champion in red_champions:
        assert not champion.available

    for champion in blue_champions:
        assert not champion.available


def test_that_champions_in_second_round_is_new(alpha: Game):
    alpha.new_round()
    played_champions = set(alpha.red.champions) | set(alpha.blue.champions)
    alpha.update_winners(alpha.red)
    alpha.new_round()

    new_champions = list(alpha.red.champions) + list(alpha.blue.champions)
    for new_champ in new_champions:
        assert new_champ not in played_champions


def test_that_save_game_create_saved_file(long_alpha: Game, save_file: str):
    long_alpha.save_game(save_file)

    saved_file = os.path.join("saves", f"{save_file}.json")
    assert os.path.exists(saved_file)


def test_that_loaded_game_has_player_1_with_score_2(
    alpha: Game, long_alpha: Game, save_file: str
):
    long_alpha.save_game(save_file)
    alpha.load_game(save_file)

    player = alpha.players[0]

    assert player.score == 2


def test_that_loaded_game_has_first_able_champion_(
    alpha: Game, long_alpha: Game, save_file: str
):
    long_alpha.save_game(save_file)
    alpha.load_game(save_file)

    for champ in alpha.champions:
        if champ.available:
            assert champ.name == "Briar"
            break
