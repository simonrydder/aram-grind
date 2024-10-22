from src.interfaces.champion import Champion
from src.utils.lol import ChampionData


class StandardChampion(Champion):
    def __init__(self, data: ChampionData) -> None:
        super().__init__()

        self._name: str = data.name

    @property
    def available(self) -> bool:
        return False

    def disable(self) -> None:
        return super().disable()

    def enable(self) -> None:
        return super().enable()

    @property
    def name(self) -> str:
        return self._name
