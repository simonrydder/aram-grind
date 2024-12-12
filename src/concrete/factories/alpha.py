from src.concrete.strategies.player_assignment.first import (
    FirstPlayerAssignemntStrategy,
)
from src.concrete.strategies.save_game.standard import StandardSaveGameStrategy
from src.interfaces.factories.game import GameFactory
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy
from src.interfaces.strategies.save_game import SaveGameStrategy


class Alpha(GameFactory):
    @property
    def player_assignment(self) -> PlayerAssignmentStrategy:
        return FirstPlayerAssignemntStrategy()

    @property
    def save_game(self) -> SaveGameStrategy:
        return StandardSaveGameStrategy()
