from src.interfaces.game import Game
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy


class FirstPlayerAssignmentStrategy(PlayerAssignmentStrategy):
    def apply(self, game: Game) -> None:
        players = iter(game.players)
        for _ in range(game.red.size):
            next_player = next(players)
            game.red.add_player(next_player)

        for _ in range(game.blue.size):
            next_player = next(players)
            game.blue.add_player(next_player)
