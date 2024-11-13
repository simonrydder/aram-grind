from src.interfaces.game import Game
from src.interfaces.strategies.player_assignment import PlayerAssignmentStrategy


class FirstPlayerAssignemntStrategy(PlayerAssignmentStrategy):
    def apply(self, game: "Game") -> None:
        players = iter(game.players)
        for _ in range(game.red.size):
            game.red.add_player(next(players))

        for _ in range(game.blue.size):
            game.blue.add_player(next(players))
