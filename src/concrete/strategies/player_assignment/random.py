import random
from typing import cast

from src.concrete.strategies.player_assignment.first import (
    FirstPlayerAssignmentStrategy,
)
from src.interfaces.game import Game
from src.interfaces.mutable_game import MutableGame
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy


class RandomPlayerAssignemntStrategy(PlayerAssignmentStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.first = FirstPlayerAssignmentStrategy()

    def apply(self, game: Game) -> None:
        players = list(game.players)
        random.shuffle(players)

        mutable_game = cast(MutableGame, game)
        mutable_game.update_players(players)

        game = cast(Game, mutable_game)
        self.first.apply(game)
