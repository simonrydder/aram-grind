from typing import Iterator

from src.interfaces.champion import Champion
from src.interfaces.game import Game
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy


class FirstChampionAssignmentStrategy(ChampionAssignmentStrategy):
    def apply(self, game: "Game", champions: Iterator["Champion"]) -> None:
        for _ in range(game.red.size):
            next_champion = next(champions)
            game.red.add_champion(next_champion)

        for _ in range(game.blue.size):
            naxt_champion = next(champions)
            game.blue.add_champion(naxt_champion)
