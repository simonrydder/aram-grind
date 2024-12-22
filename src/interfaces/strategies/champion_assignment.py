from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.interfaces.champion import Champion
    from src.interfaces.game import Game


class ChampionAssignmentStrategy(ABC):
    @abstractmethod
    def apply(self, game: "Game", champions: Sequence["Champion"]) -> None:
        pass
