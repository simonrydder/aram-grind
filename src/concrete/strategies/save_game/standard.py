import json
import os

from src.interfaces.game import Game
from src.interfaces.strategies.save_game import SaveGameStrategy
from src.states.game import GameState


class StandardSaveGameStrategy(SaveGameStrategy):
    def save(self, game: Game, file_name: str) -> None:
        state = GameState(
            players=[p.to_state() for p in game.players],
            champions=[c.to_state() for c in game.champions],
        )

        file = os.path.join("saves", f"{file_name}.json")
        with open(file, "w") as f:
            json.dump(state.model_dump(), f)
