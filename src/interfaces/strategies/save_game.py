from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.interfaces.game import Game


class SaveGameStrategy(ABC):
    @abstractmethod
    def save(self, game: "Game", file_name: str) -> None:
        pass
