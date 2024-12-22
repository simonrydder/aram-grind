from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterator

if TYPE_CHECKING:
    from src.interfaces.champion import Champion
    from src.interfaces.game import Game


class ChampionAssignmentStrategy(ABC):
    @abstractmethod
    def apply(self, game: "Game", champions: Iterator["Champion"]) -> None:
        pass
