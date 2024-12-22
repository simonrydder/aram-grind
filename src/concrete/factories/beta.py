from src.concrete.strategies.champion_assignment.first import (
    FirstChampionAssignmentStrategy,
)
from src.concrete.strategies.player_assignment.random import (
    RandomPlayerAssignemntStrategy,
)
from src.concrete.strategies.save_game.standard import StandardSaveGameStrategy
from src.interfaces.factories.game import GameFactory
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy
from src.interfaces.strategies.save_game import SaveGameStrategy


class Beta(GameFactory):
    @property
    def player_assignment(self) -> PlayerAssignmentStrategy:
        return RandomPlayerAssignemntStrategy()

    @property
    def champion_assignment(self) -> ChampionAssignmentStrategy:
        return FirstChampionAssignmentStrategy()

    @property
    def save_game(self) -> SaveGameStrategy:
        return StandardSaveGameStrategy()
