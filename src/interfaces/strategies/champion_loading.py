from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

from src.interfaces.champion import Champion

if TYPE_CHECKING:
    from src.interfaces.game import Game


class ChampionLoadingStrategy(ABC):
    @abstractmethod
    def load(self, game: "Game") -> Sequence[Champion]:
        pass
