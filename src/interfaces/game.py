from abc import ABC, abstractmethod
from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.player import Player
from src.interfaces.team import Team


class Game(ABC):
    @abstractmethod
    def __init__(self, players: Sequence[Player]) -> None:
        super().__init__()

    @property
    @abstractmethod
    def players(self) -> Sequence[Player]:
        pass

    @property
    @abstractmethod
    def champions(self) -> Sequence[Champion]:
        pass

    @property
    @abstractmethod
    def red(self) -> Team:
        pass

    @property
    @abstractmethod
    def blue(self) -> Team:
        pass

    @abstractmethod
    def new_round(self) -> None:
        pass

    @abstractmethod
    def update_winners(self, team: Team) -> None:
        pass

    @abstractmethod
    def get_scoreboard(self) -> Sequence[Player]:
        pass

    @abstractmethod
    def get_winner(self) -> Player:
        pass

    @abstractmethod
    def save_game(self, file_name: str) -> None:
        pass

    @abstractmethod
    def load_game(self, file_name: str) -> None:
        pass

    @abstractmethod
    def end_game(self) -> None:
        pass
