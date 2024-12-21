import random

from src.concrete.standard_game import StandardGame
from src.concrete.strategies.player_assignment.first import (
    FirstPlayerAssignmentStrategy,
)
from src.interfaces.game import Game
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy


class RandomPlayerAssignemntStrategy(PlayerAssignmentStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.first = FirstPlayerAssignmentStrategy()

    def apply(self, game: "Game") -> None:
        assert isinstance(game, StandardGame)
        players = list(game.players)
        random.shuffle(players)
        game.players = players

        self.first.apply(game)
        pass
