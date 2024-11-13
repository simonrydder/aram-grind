from src.concrete.strategies.player_assignment.first import (
    FirstPlayerAssignemntStrategy,
)
from src.interfaces.game import Game
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy


class RandomPlayerAssignemntStrategy(PlayerAssignmentStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.first = FirstPlayerAssignemntStrategy()

    def apply(self, game: "Game") -> None:
        # TODO: Cast game to mutable game where players can be shuffled

        # TODO: Apply first on the original game.
        pass
