from typing import Sequence

from src.concrete.standard_champion import StandardChampion
from src.interfaces.champion import Champion
from src.interfaces.game import Game
from src.interfaces.strategies.champion_loading import (
    ChampionLoadingStrategy,
)
from src.utils.lol import Language, get_champion_data, get_data_url


class FixedChampionLoadingStrategy(ChampionLoadingStrategy):
    def __init__(self, version: str = "14.19.1") -> None:
        self.version = version

    def load(self, game: Game) -> Sequence[Champion]:
        data_url = get_data_url(self.version, Language.US)
        data_dragon = get_champion_data(data_url)

        champion_dragons = data_dragon.data

        champions: Sequence[Champion] = []
        for champion_dragon in champion_dragons.values():
            champions.append(StandardChampion(champion_dragon))

        return champions
