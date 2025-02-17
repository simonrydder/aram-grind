import random
from typing import cast

from src.concrete.strategies.champion_assignment.first import (
    FirstChampionAssignmentStrategy,
)
from src.interfaces.game import Game
from src.interfaces.mutable_game import MutableGame
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy


class RandomChampionAssignmentStrategy(ChampionAssignmentStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.first = FirstChampionAssignmentStrategy()

    def apply(self, game: Game) -> None:
        champions = list(game.champions)
        random.shuffle(champions)

        mutable_game = cast(MutableGame, game)
        mutable_game.update_champions(champions)

        game = cast(Game, mutable_game)
        self.first.apply(game)
