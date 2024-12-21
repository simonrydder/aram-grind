from src.interfaces.game import Game


def test_that_players_are_shuffled(beta: Game):
    beta.new_round()
    red_players = beta.red.players
    names = [p.name for p in red_players]

    assert names != ["1", "2", "3"]
