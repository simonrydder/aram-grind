from src.concrete.standard_champion import StandardChampion


def test_that_champion_name_is_aatrox(aatrox: StandardChampion):
    assert aatrox.name == "Aatrox"


def test_that_champion_name_is_ekko(ekko: StandardChampion):
    assert ekko.name == "Ekko"


def test_that_champion_is_available_as_default(ekko: StandardChampion):
    assert ekko.available


def test_that_champion_is_unavailable_after_disable(ekko: StandardChampion):
    ekko.disable()

    assert not ekko.available


def test_that_champion_is_available_after_enable(ekko: StandardChampion):
    ekko.disable()
    ekko.enable()

    assert ekko.available
