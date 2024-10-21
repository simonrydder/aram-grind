from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.player import Player
from src.interfaces.team import Team


class TooManyPlayersError(Exception):
    pass


class TooManyChampionsError(Exception):
    pass


class StandardTeam(Team):
    def __init__(self, size: int = 3) -> None:
        super().__init__()

        self._players: Sequence[Player] = []
        self._champs: Sequence[Champion] = []
        self._size: int = size

    @property
    def players(self) -> Sequence[Player]:
        return self._players

    def add_player(self, new_player: Player) -> None:
        if len(self.players) == self.size:
            raise TooManyPlayersError

        self._players = list(self._players) + [new_player]

    @property
    def champions(self) -> Sequence[Champion]:
        return self._champs

    def add_champion(self, new_champion: Champion) -> None:
        if len(self.champions) == self.size:
            raise TooManyChampionsError

        self._champs = list(self.champions) + [new_champion]

    @property
    def size(self) -> int:
        return self._size

    def reset(self) -> None:
        self._players = []
        self._champs = []
