from src.interfaces.champion import Champion, ChampionState
from src.utils.lol import ChampionDragon


class StandardChampion(Champion):
    def __init__(self, data: ChampionDragon) -> None:
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
        state = ChampionState(available=self._available)
        return state

    def from_dict(self, state: ChampionState) -> Champion:
        self._available = state.get("available")
        return self

    @property
    def name(self) -> str:
        return self._name
