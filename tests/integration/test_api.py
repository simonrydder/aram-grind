import os
from typing import Iterator, List

import pytest
from fastapi.testclient import TestClient

from src.api import app
from src.concrete.factories.alpha import Alpha
from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.interfaces.game import Game
from tests.utils import api as api_utils


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


@pytest.fixture(scope="function")
def file() -> Iterator[str]:
    file = "file"
    yield file

    saved_file = os.path.join("saves", f"{file}.json")
    os.remove(saved_file)


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


def test_that_add_players_returns_message(client: TestClient, names: List[str]):
    client.post("/new")
    response = client.post("/new/add_players", json=names)

    assert response.json() == {"message": "Players initialized."}


def test_that_new_round_has_valid_route(client: TestClient, alpha: None):
    res = client.get("/game/new_round")

    assert res.status_code == 200


def test_that_new_round_has_valid_red_team(client: TestClient, alpha: None):
    client.get("/game/new_round")

    red = app.game.red

    assert len(red.players) == 3
    assert len(red.champions) == 3


def test_that_new_round_retuns_teams(client: TestClient, alpha: None, names: List[str]):
    res = client.get("/game/new_round")

    true_game = StandardGame(Alpha())
    true_game.initialize_game([StandardPlayer(name=name) for name in names])
    true_game.new_round()

    red_state = true_game.red.to_state()
    blue_state = true_game.blue.to_state()

    json_respons = [red_state.model_dump(), blue_state.model_dump()]

    assert res.json() == json_respons


def test_that_round_winner_has_valid_route(client: TestClient, alpha: None):
    client.get("/game/new_round")
    response = client.post("/game/round_winner", json={"team": "red"})

    assert response.status_code == 200


def test_that_round_winner_red_gives_simon_1_point(client: TestClient, alpha: None):
    client.get("/game/new_round")
    _ = client.post("/game/round_winner", json={"team": "red"})

    players = app.game.players
    simon = players[0]

    assert simon.score == 1


def test_that_round_winner_blue_gives_denze_1_point(client: TestClient, alpha: None):
    client.get("/game/new_round")
    client.post("/game/round_winner", json={"team": "blue"})

    players = app.game.players
    denze = players[3]

    assert denze.score == 1


def test_that_round_winner_with_invalid_team_raises_exception(
    client: TestClient, alpha: None
):
    client.get("/game/new_round")
    response = client.post("/game/round_winner", json={"team": "green"})

    assert response.status_code == 400


def test_that_round_winner_red_has_return_message(client: TestClient, alpha: None):
    client.get("/game/new_round")
    response = client.post("/game/round_winner", json={"team": "red"})

    assert response.json() == {"message": "Updated round winner was 'red'"}


def test_that_round_winner_blue_has_return_message(client: TestClient, alpha: None):
    client.get("/game/new_round")
    response = client.post("/game/round_winner", json={"team": "blue"})

    assert response.json() == {"message": "Updated round winner was 'blue'"}


def test_that_get_scorebard_has_valid_route(client: TestClient, alpha: None):
    response = client.get("/game/scoreboard")

    assert response.status_code == 200


def test_that_get_scoreboard_has_denze_first(client: TestClient, alpha: None):
    client = api_utils.skip_rounds(client, 2, "blue")

    response = client.get("/game/scoreboard")

    assert response.json() == [
        {"name": "Denze", "score": 2},
        {"name": "Hanghøj", "score": 2},
        {"name": "Peter", "score": 2},
        {"name": "Alex", "score": 0},
        {"name": "Eskild", "score": 0},
        {"name": "Simon", "score": 0},
    ]


def test_that_champions_has_valid_rounte(client: TestClient, alpha: None):
    response = client.get("/game/champions")

    assert response.status_code == 200


def test_that_save_game_has_valid_route(client: TestClient, alpha: None, file: str):
    client = api_utils.skip_rounds(client, 3, "red")

    response = client.post("/game/save", json={"name": file})

    assert response.status_code == 200


def test_that_champions_has_length_168(client: TestClient, alpha: None):
    response = client.get("game/champions")

    assert len(response.json()) == 168


def test_that_champions_has_lenght_168_after_one_round(client: TestClient, alpha: None):
    client = api_utils.skip_rounds(client, 1, "blue")

    response = client.get("game/champions")

    assert len(response.json()) == 168


def test_that_save_game_has_return_message(client: TestClient, alpha: None, file: str):
    client = api_utils.skip_rounds(client, 3, "red")
    response = client.post("/game/save", json={"name": file})

    assert response.json() == {"message": f"Game saved in {file}"}


def test_that_save_game_creates_saved_file(client: TestClient, alpha: None, file: str):
    client = api_utils.skip_rounds(client, 3, "red")
    _ = client.post("/game/save", json={"name": file})

    saved_file = os.path.join("saves", f"{file}.json")
    assert os.path.exists(saved_file)


# def test_that_load_game_has_valid_route(client: TestClient, file: str):
#     response = client.post(f"/load?file={file}")

#     assert response.status_code == 200
