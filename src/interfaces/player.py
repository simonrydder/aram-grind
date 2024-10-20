from abc import ABC, abstractmethod


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
