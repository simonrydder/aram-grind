from abc import ABC, abstractmethod

from src.states.champion import ChampionState


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
    def to_state(self) -> ChampionState:
        pass

    @abstractmethod
    def from_state(self, state: ChampionState) -> "Champion":
        pass
