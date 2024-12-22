from abc import ABC, abstractmethod
from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.factories.game import GameFactory
from src.interfaces.player import Player
from src.interfaces.team import Team


class Game(ABC):
    @abstractmethod
    def __init__(self, game_factory: GameFactory) -> None:
        super().__init__()
        self._player_assignment = game_factory.player_assignment
        self._champion_assignment = game_factory.champion_assignment
        self._save = game_factory.save_game

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
    def available_champions(self) -> Sequence[Champion]:
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
    def initialize_game(self, players: Sequence[Player]) -> None:
        pass

    @abstractmethod
    def new_round(self) -> None:
        pass

    @abstractmethod
    def update_winners(self, winner: Team) -> None:
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
