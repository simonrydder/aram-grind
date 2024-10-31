from typing import List, Sequence, Tuple

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.interfaces.game import Game
from src.states.player import PlayerState
from src.states.team import TeamState

app = FastAPI()

game: Game


class Message(BaseModel):
    message: str


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


@app.get("/game/new_round")
async def new_round() -> Tuple[TeamState, TeamState]:
    global game
    game.new_round()

    red = game.red
    blue = game.blue

    return (red.to_state(), blue.to_state())


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
async def get_scoreboard() -> Sequence[PlayerState]:
    global game
    players = game.get_scoreboard()

    return [p.to_state() for p in players]
