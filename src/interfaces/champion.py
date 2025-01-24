from abc import ABC, abstractmethod

from src.states.champion import ChampionState


class Champion(ABC):
    def __str__(self) -> str:
        return f"{self.name}: ({self.tags}, ({self.physical}, {self.defense}, {self.magic}, {self.difficulty}))"

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def available(self) -> bool:
        pass

    @property
    @abstractmethod
    def tags(self) -> set[str]:
        pass

    @property
    @abstractmethod
    def physical(self) -> int:
        pass

    @property
    @abstractmethod
    def defense(self) -> int:
        pass

    @property
    @abstractmethod
    def magic(self) -> int:
        pass

    @property
    @abstractmethod
    def difficulty(self) -> int:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def to_state(self) -> ChampionState:
        pass

    @abstractmethod
    def from_state(self, state: ChampionState) -> "Champion":
        pass
