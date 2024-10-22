import pytest

from src.concrete.standard_player import StandardPlayer
from src.interfaces.player import PlayerState


def test_player_has_name_p1():
    player = StandardPlayer("p1")

    assert player.name == "p1"


def test_player_has_name_p2():
    player = StandardPlayer("p2")

    assert player.name == "p2"


def test_player_has_score_0():
    player = StandardPlayer("")

    assert player.score == 0


def test_player_score_can_be_updated_to_4():
    player = StandardPlayer("")

    new_score = 4
    player.score = new_score

    assert player.score == new_score


def test_player_score_can_be_updated_to_3():
    player = StandardPlayer("")

    new_score = 3
    player.score = new_score

    assert player.score == new_score


def test_player_score_can_not_be_negative():
    player = StandardPlayer("")

    new_score = -1
    with pytest.raises(ValueError):
        player.score = new_score


def test_that_player_state_has_key_name():
    player = StandardPlayer("1")
    state = player.to_dict()

    assert "name" in state.keys()


def test_that_player_state_has_name_value_1():
    player = StandardPlayer("1")
    state = player.to_dict()

    assert state.get("name") == "1"


def test_that_player_state_has_key_score():
    p = StandardPlayer("1")
    state = p.to_dict()

    assert "score" in state.keys()


def test_that_player_state_has_score_value_2():
    p = StandardPlayer("1")
    p.score = 2
    state = p.to_dict()

    assert state.get("score") == 2


def test_that_player_from_state_has_name_p2():
    state = PlayerState(name="p2", score=0)
    p = StandardPlayer("").from_dict(state)

    assert p.name == "p2"


def test_that_player_from_dict_has_score_3():
    state = PlayerState(name="p1", score=3)
    p = StandardPlayer("").from_dict(state)

    assert p.score == 3
