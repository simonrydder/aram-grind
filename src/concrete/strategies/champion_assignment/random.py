from src.interfaces.game import Game
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy


class RandomChampionAssignmentStrategy(ChampionAssignmentStrategy):
    def apply(self, game: Game) -> None:
        return super().apply(game)
