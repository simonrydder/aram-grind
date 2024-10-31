from abc import ABC, abstractmethod

from src.states.player import PlayerState


class Player(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def score(self) -> int:
        pass

    @score.setter
    @abstractmethod
    def score(self, new_score: int) -> None:
        pass

    @abstractmethod
    def to_state(self) -> PlayerState:
        pass

    @abstractmethod
    def from_state(self, state: PlayerState) -> "Player":
        pass
