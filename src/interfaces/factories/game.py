from abc import ABC, abstractmethod

from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy
from src.interfaces.strategies.save_game import SaveGameStrategy


class GameFactory(ABC):
    @property
    @abstractmethod
    def player_assignment(self) -> PlayerAssignmentStrategy:
        pass

    @property
    @abstractmethod
    def champion_assignment(self) -> ChampionAssignmentStrategy:
        pass

    @property
    @abstractmethod
    def save_game(self) -> SaveGameStrategy:
        pass
