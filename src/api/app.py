from typing import List, Sequence, Tuple

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.interfaces.game import Game

app = FastAPI()

game: Game


class Message(BaseModel):
    message: str


class PlayerData(BaseModel):
    name: str
    score: int


@app.get("/")
async def root() -> str:
    return "Hello, World!"


@app.post("/new")
async def create_game() -> Message:
    global game
    game = StandardGame()

    return Message(message="Game initialized successfully")


@app.post("/new/add_players")
async def add_players(names: List[str]) -> None:
    global game
    players = [StandardPlayer(name) for name in names]
    game.initialize_game(players)
    return None


class TeamData(BaseModel):
    players: Sequence[str]
    champions: Sequence[str]


@app.get("/game/new_round")
async def new_round() -> Tuple[TeamData, TeamData]:
    global game
    game.new_round()

    red = game.red
    players = [player.name for player in red.players]
    champions = [champion.name for champion in red.champions]
    red_data = TeamData(players=players, champions=champions)

    blue = game.blue
    players = [player.name for player in blue.players]
    champions = [champion.name for champion in blue.champions]
    blue_data = TeamData(players=players, champions=champions)

    return (red_data, blue_data)


@app.post("/game/round_winner")
async def round_winner(team: str) -> Message:
    global game
    print(team)
    if team.lower() == "red":
        game.update_winners(game.red)
    elif team.lower() == "blue":
        game.update_winners(game.blue)
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid team name. Valid options ['red', 'blue']",
        )

    return Message(message=f"Updated round winner was '{team}'")


@app.get("/game/scoreboard")
async def get_scoreboard() -> Sequence[PlayerData]:
    global game
    players = game.get_scoreboard()

    return [PlayerData(name=p.name, score=p.score) for p in players]
