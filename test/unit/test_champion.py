from src.concrete.standard_champion import StandardChampion


def test_that_champion_name_is_aatrox(aatrox: StandardChampion):
    assert aatrox.name == "Aatrox"


def test_that_champion_name_is_ekko(ekko: StandardChampion):
    assert ekko.name == "Ekko"
