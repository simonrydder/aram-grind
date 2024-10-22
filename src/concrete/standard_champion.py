from src.interfaces.champion import Champion, ChampionState
from src.utils.lol import ChampionData


class StandardChampion(Champion):
    def __init__(self, data: ChampionData) -> None:
        super().__init__()

        self._available: bool = True
        self._name: str = data.name

    @property
    def available(self) -> bool:
        return self._available

    def disable(self) -> None:
        self._available = False

    def enable(self) -> None:
        self._available = True

    def to_dict(self) -> ChampionState:
        return super().to_dict()

    def from_dict(self, state: ChampionState) -> Champion:
        return super().from_dict(state)

    @property
    def name(self) -> str:
        return self._name
