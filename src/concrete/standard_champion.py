from src.interfaces.champion import Champion, ChampionState
from src.utils.lol import BASE_URL, ChampionDragon


class StandardChampion(Champion):
    def __init__(self, data: ChampionDragon) -> None:
        super().__init__()

        self._available: bool = True
        self._name: str = data.name
        self._image: str = self._get_image_url(data.image.full, data.version)
        self._loading: str = self._get_loading_image(data.id)

    @property
    def name(self) -> str:
        return self._name

    @property
    def available(self) -> bool:
        return self._available

    def disable(self) -> None:
        self._available = False

    def enable(self) -> None:
        self._available = True

    def to_state(self) -> ChampionState:
        state = ChampionState(
            name=self._name,
            available=self._available,
            image=self._image,
            loading=self._loading,
        )
        return state

    def from_state(self, state: ChampionState) -> Champion:
        self._available = state.available
        return self

    def _get_image_url(self, image: str, version: str) -> str:
        return f"{BASE_URL}cdn/{version}/img/champion/{image}"

    def _get_loading_image(self, id: str) -> str:
        return f"{BASE_URL}cdn/img/champion/loading/{id}_0.jpg"
