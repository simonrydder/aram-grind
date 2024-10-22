from abc import ABC, abstractmethod
from typing import TypedDict


class ChampionState(TypedDict):
    available: bool


class Champion(ABC):
    @property
    @abstractmethod
    def available(self) -> bool:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> ChampionState:
        pass

    @abstractmethod
    def from_dict(self, state: ChampionState) -> "Champion":
        pass
