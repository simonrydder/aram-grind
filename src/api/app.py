from typing import List

from fastapi import FastAPI

from src.concrete.standard_game import StandardGame
from src.concrete.standard_player import StandardPlayer
from src.interfaces.game import Game

app = FastAPI()

game: Game


@app.get("/")
async def root():
    return "Hello, World!"


@app.post("/new")
async def create_game():
    global game
    game = StandardGame()

    return {"message": "Game initialized successfully"}


@app.post("/new/add_players")
async def add_players(names: List[str]):
    global game
    players = [StandardPlayer(name) for name in names]
    game.initialize_game(players)
    return None


@app.get("/game/new_round")
async def new_round():
    global game
    game.new_round()
    pass


#     global game
#     players = [StandardPlayer(name) for name in names]
#     game.initialize_game(players)

#     return "Players added successfully"
