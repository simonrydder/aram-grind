from typing import Iterator, List

import pytest
from fastapi.testclient import TestClient

from src.api import app
from src.interfaces.game import Game


@pytest.fixture(scope="function")
def client() -> Iterator[TestClient]:
    yield TestClient(app.app)
    app.game = None


@pytest.fixture(scope="function")
def names() -> Iterator[List[str]]:
    yield ["Simon", "Alex", "Eskild", "Denze", "Hanghøj", "Peter"]


@pytest.fixture(scope="function")
def alpha(client: TestClient, names: List[str]) -> None:
    client.post("/new")
    client.post("/new/add_players", json=names)


def test_that_root_is_active_and_game_is_none(client: TestClient):
    response = client.get("/")

    assert response.status_code == 200


def test_that_create_game_has_valid_route(client: TestClient):
    response = client.post("/new")

    assert response.status_code == 200


def test_create_game_return_message(client: TestClient):
    response = client.post("/new")

    assert response.json() == {"message": "Game initialized successfully"}


def test_that_create_game_initialize_a_game(client: TestClient):
    _ = client.post("/new")

    assert isinstance(app.game, Game)


def test_that_add_players_as_valid_route(client: TestClient, names: List[str]):
    client.post("/new")
    response = client.post("/new/add_players", json=names)

    assert response.status_code == 200


def test_that_add_players_initialize_game(client: TestClient, names: List[str]):
    client.post("/new")
    _ = client.post("/new/add_players", json=names)

    assert len(app.game.players) == 6


def test_that_new_round_has_valid_route(client: TestClient, alpha: None):
    res = client.get("/game/new_round")

    assert res.status_code == 200


def test_that_new_round_has_valid_red_team(client: TestClient, alpha: None):
    client.get("/game/new_round")

    red = app.game.red

    assert len(red.players) == 3
    assert len(red.champions) == 3


def test_that_new_round_retuns_teams(client: TestClient, alpha: None):
    res = client.get("/game/new_round")

    json_respons = {
        "red": {"players": ["Simon", "Alex", "Eskild"], "champions": ["Aatrox"]}
    }

    assert res.json() == json_respons
