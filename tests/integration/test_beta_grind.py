from src.interfaces.game import Game


def test_that_players_are_shuffled(beta: Game):
    beta.new_round()
    red_players = beta.red.players
    names = [p.name for p in red_players]

    assert names != ["1", "2", "3"]


def test_that_champions_are_shuffled(beta: Game):
    beta.new_round()
    champs = beta.red.champions
    names = [c.name for c in champs]

    assert names != ["Aatrox", "Ahri", "Akali"]
