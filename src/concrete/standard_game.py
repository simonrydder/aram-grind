from math import ceil, floor
from typing import Sequence

from src.concrete.standard_champion import StandardChampion
from src.concrete.standard_team import StandardTeam
from src.interfaces.champion import Champion
from src.interfaces.game import Game
from src.interfaces.player import Player
from src.interfaces.team import Team
from src.utils.lol import Language, get_champion_data, get_data_url


class StandardGame(Game):

    def __init__(self, players: Sequence[Player]) -> None:
        super().__init__(players)
        self._players = players

        self._red = StandardTeam(ceil(len(players) / 2))
        self._blue = StandardTeam(floor(len(players) / 2))

        data_url = get_data_url("14.19.1", Language.US)
        data = get_champion_data(data_url)
        self._champions = [StandardChampion(cd) for _, cd in data.data.items()]

    @property
    def players(self) -> Sequence[Player]:
        return self._players

    @property
    def champions(self) -> Sequence[Champion]:
        return self._champions

    @property
    def red(self) -> Team:
        return self._red

    @property
    def blue(self) -> Team:
        return self._blue

    def new_round(self) -> None:
        return super().new_round()

    def update_winners(self, team: Team) -> None:
        return super().update_winners(team)

    def get_scoreboard(self) -> Sequence[Player]:
        return super().get_scoreboard()

    def get_winner(self) -> Player:
        return super().get_winner()

    def save_game(self, file_name: str) -> None:
        return super().save_game(file_name)

    def load_game(self, file_name: str) -> None:
        return super().load_game(file_name)

    def end_game(self) -> None:
        return super().end_game()


if __name__ == "__main__":
    StandardGame([])
