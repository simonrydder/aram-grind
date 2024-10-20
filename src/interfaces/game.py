from abc import ABC, abstractmethod
from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.player import Player
from src.interfaces.team import Team


class Game(ABC):
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
    def get_team_players(self, team: Team) -> Sequence[Player]:
        pass

    @abstractmethod
    def get_team_champions(self, team: Team) -> Sequence[Champion]:
        pass

    @abstractmethod
    def update_winners(self, team: Team) -> None:
        pass

    @abstractmethod
    def get_score(self, player: Player) -> int:
        pass

    @abstractmethod
    def get_scoreboard(self) -> Sequence[tuple[str, int]]:
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
