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


def test_that_champion_state_has_available_true(ekko: Champion):
    state = ekko.to_state()

    assert state.available


def test_that_champion_from_state_is_not_available(ekko: Champion):
    state = ChampionState(name=ekko.name, available=False)
    ekko.from_state(state)

    assert not ekko.available


def test_that_ekko_state_has_image(ekko: Champion):
    state = ekko.to_state()
    image = "https://ddragon.leagueoflegends.com/cdn/14.19.1/img/champion/Ekko.png"

    assert state.image == image


def test_that_aatrox_state_has_image(aatrox: Champion):
    state = aatrox.to_state()
    image = "https://ddragon.leagueoflegends.com/cdn/14.19.1/img/champion/Aatrox.png"

    assert state.image == image


def test_that_ekko_state_has_loading_image(ekko: Champion):
    state = ekko.to_state()
    loading_image = (
        "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Ekko_0.jpg"
    )

    assert state.loading == loading_image


def test_that_aatrox_state_has_loading_image(aatrox: Champion):
    state = aatrox.to_state()
    loading_image = (
        "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Aatrox_0.jpg"
    )

    assert state.loading == loading_image


def test_that_aatrox_has_tags_fighter(aatrox: Champion):
    assert aatrox.tags == {"Fighter"}


def test_that_ekko_has_tags_mage_and_assasin(ekko: Champion):
    assert ekko.tags == {"Mage", "Assassin"}


def test_that_aatrox_has_physical_8(aatrox: Champion):
    assert aatrox.physical == 8


def test_that_ekko_has_physical_4(ekko: Champion):
    assert ekko.physical == 5


def test_that_aatrox_has_defense_4(aatrox: Champion):
    assert aatrox.defense == 4


def test_that_ekko_has_defense_3(ekko: Champion):
    assert ekko.defense == 3


def test_that_aatrox_has_magic_3(aatrox: Champion):
    assert aatrox.magic == 3


def test_that_ekko_has_magic_7(ekko: Champion):
    assert ekko.magic == 7


def test_that_aatrox_has_difficulty_4(aatrox: Champion):
    assert aatrox.difficulty == 4


def test_that_ekko_has_difficulty_8(ekko: Champion):
    assert ekko.difficulty == 8
