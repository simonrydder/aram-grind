from itertools import combinations
from math import sqrt
from typing import Sequence

from src.concrete.strategies.champion_assignment.tag_based import (
    NotEnoughTagGroups,
    TagBasedChampionAssignment,
)
from src.interfaces.champion import Champion
from src.interfaces.game import Game
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy

type Rating = tuple[int, int, int, int]


class BalancedChampionAssignment(ChampionAssignmentStrategy):
    def __init__(self) -> None:
        self.tag_based = TagBasedChampionAssignment()
        self.weight: dict[str, float] = {
            "physical": 1,
            "defence": 1,
            "magic": 1,
            "difficulty": 0.1,
        }

    def apply(self, game: Game) -> None:
        assert game.red.size == game.blue.size, "This strategy requires equal team size"
        available_champions = game.available_champions

        try:
            self.main_apply_method(game, available_champions)
        except NotEnoughTagGroups:
            self.exception_apply_method(game, available_champions)

    def main_apply_method(self, game: Game, champions: Sequence[Champion]) -> None:
        tag_count = self.tag_based.generate_tag_count(champions)
        available_tags = self.tag_based.filter_available_tags(tag_count)
        tags = self.tag_based.select_tags(available_tags, count=game.red.size)
        filtered_champions = self.tag_based.filter_champions(champions, tags)

        for champions in filtered_champions.values():
            red_champ, blue_champ = self.get_closest_pair(champions)
            game.red.add_champion(red_champ)
            game.blue.add_champion(blue_champ)

    def exception_apply_method(self, game: Game, champions: Sequence[Champion]) -> None:
        champions = list(champions)
        for _ in range(game.red.size):
            red_champ, blue_champ = self.get_closest_pair(champions)
            game.red.add_champion(red_champ)
            game.blue.add_champion(blue_champ)

            champions.remove(red_champ)
            champions.remove(blue_champ)

    def calculate_rating_distance(self, a: Champion, b: Champion) -> float:
        """Calculate a weighted euclidian distance between the rating of two champions."""

        return sqrt(
            self.weight["physical"] * (a.physical - b.physical) ** 2
            + self.weight["defence"] * (a.defense - b.defense) ** 2
            + self.weight["magic"] * (a.magic - b.magic) ** 2
            + self.weight["difficulty"] * (a.difficulty - b.difficulty) ** 2
        )

    def get_closest_pair(
        self, champions: Sequence[Champion]
    ) -> tuple[Champion, Champion]:
        closest_pair: tuple[Champion, Champion] | None = None
        min_distance = float("inf")

        for a, b in combinations(champions, 2):
            distance = self.calculate_rating_distance(a, b)

            if distance >= min_distance:
                continue

            min_distance = distance
            closest_pair = (a, b)

        assert isinstance(closest_pair, tuple), "Did not find any pairs"

        red, blue = closest_pair
        print(f"Red: {red}")
        print(f"Blue: {blue}")
        return closest_pair
