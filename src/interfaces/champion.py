from abc import ABC, abstractmethod


class Champion(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
