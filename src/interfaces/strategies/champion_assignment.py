from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.interfaces.game import Game


class ChampionAssignmentStrategy(ABC):
    @abstractmethod
    def apply(self, game: "Game") -> None:
        pass
