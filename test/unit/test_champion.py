from src.interfaces.champion import Champion, ChampionState


def test_that_champion_name_is_aatrox(aatrox: Champion):
    assert aatrox.name == "Aatrox"


def test_that_champion_name_is_ekko(ekko: Champion):
    assert ekko.name == "Ekko"


def test_that_champion_is_available_as_default(ekko: Champion):
    assert ekko.available


def test_that_champion_is_unavailable_after_disable(ekko: Champion):
    ekko.disable()

    assert not ekko.available


def test_that_champion_is_available_after_enable(ekko: Champion):
    ekko.disable()
    ekko.enable()

    assert ekko.available


def test_that_champion_dict_has_available(ekko: Champion):
    dct = ekko.to_dict()

    assert "available" in dct


def test_that_champion_state_has_available_true(ekko: Champion):
    dct = ekko.to_dict()

    assert dct.get("available")


def test_that_champion_from_state_is_not_available(ekko: Champion):
    state = ChampionState(available=False)
    ekko.from_dict(state)

    assert not ekko.available
