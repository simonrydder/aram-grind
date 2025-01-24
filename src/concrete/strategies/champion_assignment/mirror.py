from src.interfaces.game import Game
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy


class MirrorChampionAssignmentStrategy(ChampionAssignmentStrategy):
    def apply(self, game: Game) -> None:
        champs = iter(game.available_champions)
        assert game.red.size == game.blue.size

        round_champs = [next(champs) for _ in range(game.red.size)]

        for champ in round_champs:
            game.red.add_champion(champ)

        for champ in round_champs:
            game.blue.add_champion(champ)
