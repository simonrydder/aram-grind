from abc import ABC, abstractmethod
from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.player import Player


class Team(ABC):

    @property
    @abstractmethod
    def players(self) -> Sequence[Player]:
        pass

    # @players.setter
    # @abstractmethod
    # def players(self, new_players: Sequence[Player]) -> None:
    #     pass

    @abstractmethod
    def add_player(self, new_player: Player) -> None:
        pass

    @property
    @abstractmethod
    def champions(self) -> Sequence[Champion]:
        pass

    # @champions.setter
    # @abstractmethod
    # def champions(self, new_champions: Sequence[Champion]) -> None:
    #     pass

    @abstractmethod
    def add_champion(self, new_champion: Champion) -> None:
        pass

    @property
    @abstractmethod
    def size(self) -> int:
        pass
