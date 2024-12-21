from abc import ABC, abstractmethod
from typing import Sequence

from src.interfaces.player import Player


class MutableGame(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def update_players(self, new_players: Sequence[Player]) -> None:
        pass
