import json
from copy import deepcopy
from math import ceil, floor
from typing import Sequence

from src.concrete.standard_champion import StandardChampion
from src.concrete.standard_player import StandardPlayer
from src.concrete.standard_team import StandardTeam
from src.interfaces.champion import Champion, ChampionState
from src.interfaces.game import Game, GameState
from src.interfaces.player import Player, PlayerState
from src.interfaces.team import Team
from src.utils.lol import Language, get_champion_data, get_data_url


class StandardGame(Game):

    def __init__(self) -> None:
        super().__init__()
        self.initialize_game([])

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

    def initialize_game(self, players: Sequence[Player]) -> None:
        self._players = deepcopy(players)

        self._red = StandardTeam(ceil(len(self._players) / 2))
        self._blue = StandardTeam(floor(len(self._players) / 2))

        self._initialize_champions()

    def _initialize_champions(self) -> None:
        data_url = get_data_url("14.19.1", Language.US)
        data = get_champion_data(data_url)
        self._champions = [StandardChampion(cd) for _, cd in data.data.items()]

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
        game_state: GameState = {
            "players": [p.to_dict() for p in self._players],
            "champions": {c.name: c.to_dict() for c in self._champions},
        }

        with open(file_name, "w") as f:
            json.dump(game_state, f)

    def load_game(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            game_state: GameState = json.load(f)

        self._load_player_states(game_state.get("players"))
        self._load_champion_states(game_state.get("champions"))

    def _load_player_states(self, player_states: Sequence[PlayerState]):
        self._players = [StandardPlayer().from_dict(ps) for ps in player_states]

    def _load_champion_states(self, champion_states: dict[str, ChampionState]):
        for champ in self._champions:
            state = champion_states.get(champ.name)
            if state is None:
                continue

            champ.from_dict(state)

    def end_game(self) -> None:
        return super().end_game()


if __name__ == "__main__":
    StandardGame()
