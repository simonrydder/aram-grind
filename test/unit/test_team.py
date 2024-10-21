from typing import Callable, Iterator

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


@pytest.fixture(scope="function")
def aatrox(champ_name: Callable[[str], Champion]) -> Iterator[Champion]:
    yield champ_name("Aatrox")


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


def test_team_has_1_champion(aatrox):
    team = StandardTeam(1)
    team.add_champion(aatrox)

    assert len(team.champions) == 1


def test_team_has_2_champions(aatrox):
    team = StandardTeam(2)
    team.add_champion(aatrox)
    team.add_champion(aatrox)

    assert len(team.champions) == 2


def test_team_are_not_allowed_second_champion(aatrox):
    team = StandardTeam(1)
    team.add_champion(aatrox)

    with pytest.raises(TooManyChampionsError):
        team.add_champion(aatrox)


def test_team_has_no_players_after_reset():
    team = StandardTeam(2)
    team.add_player(StandardPlayer())
    team.reset()

    assert len(team.players) == 0


def test_team_has_no_champions_after_reset(aatrox):
    team = StandardTeam(2)
    team.add_champion(aatrox)
    team.reset()

    assert len(team.champions) == 0
