from src.interfaces.champion import Champion
from src.utils.lol import ChampionData


class StandardChampion(Champion):
    def __init__(self, data: ChampionData) -> None:
        super().__init__()

        self._name: str = data.name

    @property
    def name(self) -> str:
        return self._name
