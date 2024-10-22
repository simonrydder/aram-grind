from abc import ABC, abstractmethod
from typing import TypedDict


class PlayerState(TypedDict):
    name: str
    score: int


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
    def to_dict(self) -> PlayerState:
        pass

    @abstractmethod
    def from_dict(self, state: PlayerState) -> "Player":
        pass
