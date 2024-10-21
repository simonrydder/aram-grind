from typing import Callable

from src.interfaces.champion import Champion


def test_first_champion_name_is_aatrox(champ_int: Callable[[int], Champion]) -> None:
    first_champ = champ_int(0)

    assert first_champ.name == "Aatrox"


def test_20th_champion_name_is_(champ_int: Callable[[int], Champion]) -> None:
    champ_30 = champ_int(19)

    assert champ_30.name == "Caitlyn"
