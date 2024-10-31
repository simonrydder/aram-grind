from typing import Iterator

import pytest

from src.concrete.standard_player import StandardPlayer
from src.concrete.standard_team import (
    StandardTeam,
    TooManyChampionsError,
    TooManyPlayersError,
)
from src.interfaces.champion import Champion
from src.interfaces.player import Player
from src.interfaces.team import Team


@pytest.fixture(scope="function")
def team() -> Iterator[Team]:
    yield StandardTeam()


@pytest.fixture(scope="function")
def player() -> Iterator[Player]:
    yield StandardPlayer("")


def test_team_has_size_1():
    team = StandardTeam(1)

    assert team.size == 1


def test_team_has_size_2():
    team = StandardTeam(2)

    assert team.size == 2


def test_team_has_no_players():
    team = StandardTeam(1)

    assert len(team.players) == 0


def test_team_has_1_player():
    team = StandardTeam(1)
    team.add_player(StandardPlayer())

    assert len(team.players) == 1


def test_team_has_2_players():
    team = StandardTeam(2)
    team.add_player(StandardPlayer())
    team.add_player(StandardPlayer())

    assert len(team.players) == 2


def test_team_are_not_allowed_second_player():
    team = StandardTeam(1)
    team.add_player(StandardPlayer())

    with pytest.raises(TooManyPlayersError):
        team.add_player(StandardPlayer())


def test_team_has_1_champion(aatrox: Champion):
    team = StandardTeam(1)
    team.add_champion(aatrox)

    assert len(team.champions) == 1


def test_team_has_2_champions(aatrox: Champion):
    team = StandardTeam(2)
    team.add_champion(aatrox)
    team.add_champion(aatrox)

    assert len(team.champions) == 2


def test_team_are_not_allowed_second_champion(aatrox: Champion):
    team = StandardTeam(1)
    team.add_champion(aatrox)

    with pytest.raises(TooManyChampionsError):
        team.add_champion(aatrox)


def test_team_has_no_players_after_reset():
    team = StandardTeam(2)
    team.add_player(StandardPlayer())
    team.reset()

    assert len(team.players) == 0


def test_team_has_no_champions_after_reset(aatrox: Champion):
    team = StandardTeam(2)
    team.add_champion(aatrox)
    team.reset()

    assert len(team.champions) == 0


def test_team_state_has_players_attribute():
    team = StandardTeam(2)
    state = team.to_state()

    assert state.players == []


def test_team_state_has_player_state_p1():
    team = StandardTeam(2)
    p1 = StandardPlayer("1")
    team.add_player(p1)

    state = team.to_state()

    assert state.players == [p1.to_state()]


def test_team_state_has_attribute_champions(aatrox: Champion):
    team = StandardTeam(2)
    state = team.to_state()

    assert state.champions == []


def test_team_state_has_champion_state_aatrox(aatrox: Champion):
    team = StandardTeam(2)
    team.add_champion(aatrox)

    state = team.to_state()

    assert state.champions == [aatrox.to_state()]
