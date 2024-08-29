from src.lol.champion_data import ChampionData


def test_champion_data_has_id(aatrox: ChampionData):
    assert aatrox.id == "Aatrox"


def test_champion_data_has_name(aatrox: ChampionData):
    assert aatrox.name == "Aatrox"
