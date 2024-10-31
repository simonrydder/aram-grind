from abc import ABC, abstractmethod
from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.player import Player
from src.states.team import TeamState


class Team(ABC):
    @property
    @abstractmethod
    def players(self) -> Sequence[Player]:
        pass

    @abstractmethod
    def add_player(self, new_player: Player) -> None:
        pass

    @property
    @abstractmethod
    def champions(self) -> Sequence[Champion]:
        pass

    @abstractmethod
    def add_champion(self, new_champion: Champion) -> None:
        pass

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def to_state(self) -> TeamState:
        pass
