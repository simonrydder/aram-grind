from typing import Sequence

from src.concrete.strategies.champion_loading.fixed import FixedChampionLoadingStrategy
from src.interfaces.champion import Champion
from src.interfaces.game import Game
from src.interfaces.strategies.champion_loading import (
    ChampionLoadingStrategy,
)
from src.utils.lol import fetch_versions, get_latest_version


class LatestChampionLoadingStrategy(ChampionLoadingStrategy):
    def __init__(self) -> None:
        versions = fetch_versions()
        self.version = get_latest_version(versions)
        self.fixed = FixedChampionLoadingStrategy(version=self.version)

    def load(self, game: Game) -> Sequence[Champion]:
        return self.fixed.load(game)
