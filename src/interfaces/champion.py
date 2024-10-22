from abc import ABC, abstractmethod


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
