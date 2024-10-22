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

        return [champ for champ in self._champions if champ.available]

    @property
    def red(self) -> Team:
        return self._red

    @property
    def blue(self) -> Team:
        return self._blue

    def new_round(self) -> None:
        self._assign_players()
        self._assign_champions()

    def _assign_champions(self):
        champions = iter(self.champions)
        for _ in range(self.red.size):
            self.red.add_champion(next(champions))

        for _ in range(self.blue.size):
            self.blue.add_champion(next(champions))

    def _assign_players(self) -> None:
        players = iter(self.players)
        for _ in range(self.red.size):
            self.red.add_player(next(players))

        for _ in range(self.blue.size):
            self.blue.add_player(next(players))

    def update_winners(self, winner: Team) -> None:
        loser = self._get_opposite_team(winner)

        self._update_team_score(winner)

        self._disable_team_champions(winner)
        self._disable_team_champions(loser)

        winner.reset()
        loser.reset()

    def _update_team_score(self, team: Team):
        for player in team.players:
            player.score += 1

    def _get_opposite_team(self, team: Team) -> Team:
        return self.blue if team == self.red else self.red

    def _disable_team_champions(self, team: Team) -> None:
        for champ in team.champions:
            champ.disable()

    def get_scoreboard(self) -> Sequence[Player]:
        return sorted(self.players, key=lambda p: p.score, reverse=True)

    def get_winner(self) -> Player:
        score_board = self.get_scoreboard()
        return score_board[0]

    def save_game(self, file_name: str) -> None:
        return super().save_game(file_name)

    def load_game(self, file_name: str) -> None:
        return super().load_game(file_name)

    def end_game(self) -> None:
        return super().end_game()


if __name__ == "__main__":
    StandardGame([])
