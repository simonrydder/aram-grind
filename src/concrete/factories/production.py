from src.concrete.strategies.champion_assignment.balanced import (
    BalancedChampionAssignment,
)
from src.concrete.strategies.champion_loading.latest import (
    LatestChampionLoadingStrategy,
)
from src.concrete.strategies.player_assignment.random import (
    RandomPlayerAssignemntStrategy,
)
from src.concrete.strategies.save_game.standard import StandardSaveGameStrategy
from src.interfaces.factories.game import GameFactory
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy
from src.interfaces.strategies.champion_loading import ChampionLoadingStrategy
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy
from src.interfaces.strategies.save_game import SaveGameStrategy


class Production(GameFactory):
    @property
    def player_assignment(self) -> PlayerAssignmentStrategy:
        return RandomPlayerAssignemntStrategy()

    @property
    def champion_assignment(self) -> ChampionAssignmentStrategy:
        return BalancedChampionAssignment()

    @property
    def save_game(self) -> SaveGameStrategy:
        return StandardSaveGameStrategy()

    @property
    def champion_loading(self) -> ChampionLoadingStrategy:
        return LatestChampionLoadingStrategy()
