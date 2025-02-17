import json
import os
from copy import deepcopy
from math import ceil, floor
from typing import Sequence

from src.concrete.standard_player import StandardPlayer
from src.concrete.standard_team import StandardTeam
from src.interfaces.champion import Champion, ChampionState
from src.interfaces.factories.game import GameFactory
from src.interfaces.game import Game
from src.interfaces.mutable_game import MutableGame
from src.interfaces.player import Player, PlayerState
from src.interfaces.team import Team
from src.states.game import GameState


class StandardGame(Game, MutableGame):
    def __init__(self, game_factory: GameFactory) -> None:
        super().__init__(game_factory)
        self.initialize_game([])

    @property
    def players(self) -> Sequence[Player]:
        return self._players

    def update_players(self, new_players: Sequence[Player]) -> None:
        self._players = new_players

    @property
    def champions(self) -> Sequence[Champion]:
        sorted_champions = sorted(self._champions, key=lambda c: (c.available, c.name))
        return sorted_champions

    def update_champions(self, new_champions: Sequence[Champion]) -> None:
        self._champions = new_champions

    @property
    def available_champions(self) -> Sequence[Champion]:
        return [champ for champ in self._champions if champ.available]

    @property
    def red(self) -> Team:
        return self._red

    @property
    def blue(self) -> Team:
        return self._blue

    def initialize_game(self, players: Sequence[Player]) -> None:
        self._players = deepcopy(players)

        self._initialize_teams()
        self._initialize_champions()

    def _initialize_teams(self):
        self._red = StandardTeam(ceil(len(self._players) / 2))
        self._blue = StandardTeam(floor(len(self._players) / 2))

    def _initialize_champions(self) -> None:
        champions = self._champion_loading.load(self)
        # data_url = get_data_url("14.19.1", Language.US)
        # data = get_champion_data(data_url)
        # champions = [StandardChampion(cd) for cd in data.data.values()]
        self._champions = champions

    def new_round(self) -> None:
        self._assign_players()
        self._assign_champions()

    def _assign_champions(self):
        self._champion_assignment.apply(self)

    def _assign_players(self) -> None:
        self._player_assignment.apply(self)

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
        return sorted(self.players, key=lambda p: (-p.score, p.name))

    def get_winner(self) -> Player:
        score_board = self.get_scoreboard()
        return score_board[0]

    def save_game(self, file_name: str) -> None:
        self._save.save(self, file_name)

    def load_game(self, file_name: str) -> None:
        file = os.path.join("saves", f"{file_name}.json")
        with open(file, "r") as f:
            game_state = GameState(**json.load(f))

        self._load_player_states(game_state.players)
        self._load_champion_states(game_state.champions)
        self._initialize_teams()

    def _load_player_states(self, player_states: Sequence[PlayerState]):
        self._players = [StandardPlayer().from_state(ps) for ps in player_states]

    def _load_champion_states(self, champion_states: Sequence[ChampionState]):
        for champ in self._champions:
            state = next(
                (state for state in champion_states if state.name == champ.name), None
            )
            if state is None:
                continue

            champ.from_state(state)

    def end_game(self) -> None:
        return super().end_game()
