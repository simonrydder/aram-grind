from src.interfaces.game import Game
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy


class FirstChampionAssignmentStrategy(ChampionAssignmentStrategy):
    def apply(self, game: Game) -> None:
        champs = iter(game.available_champions)
        for _ in range(game.red.size):
            next_champion = next(champs)
            game.red.add_champion(next_champion)

        for _ in range(game.blue.size):
            naxt_champion = next(champs)
            game.blue.add_champion(naxt_champion)
