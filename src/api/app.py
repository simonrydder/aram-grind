from typing import List, Sequence, Tuple

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.concrete.strategies.player_assignment.first import (
    FirstPlayerAssignemntStrategy,
)
from src.interfaces.game import Game
from src.states.champion import ChampionState
from src.states.player import PlayerState
from src.states.team import TeamState

app = FastAPI()

# Configure allowed origins
origins = [
    "http://localhost:3000",
    "*",
    # add other origins if needed
]

# Apply CORS settings to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (e.g., GET, POST)
    allow_headers=["*"],  # allow all headers
)


game: Game = StandardGame(FirstPlayerAssignemntStrategy())


class Message(BaseModel):
    message: str


@app.get("/")
async def root() -> str:
    return "Hello, World!"


@app.post("/new")
async def create_game() -> Message:
    global game
    game = StandardGame(FirstPlayerAssignemntStrategy())

    return Message(message="Game initialized successfully")


@app.post("/new/add_players")
async def add_players(names: List[str]) -> Message:
    global game
    players = [StandardPlayer(name) for name in names]
    game.initialize_game(players)
    return Message(message="Players initialized.")


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


@app.get("/game/champions")
async def get_champions() -> Sequence[ChampionState]:
    global game

    return [champ.to_state() for champ in game.champions]


@app.post("/game/save")
async def save_game(file: str) -> Message:
    global game

    game.save_game(file)

    return Message(message="Game saved")


@app.post("/load")
async def load_game(file: str) -> Message:
    return Message(message=f"{file} loaded")
