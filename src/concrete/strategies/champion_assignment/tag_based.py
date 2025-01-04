import random
from typing import Sequence

from src.interfaces.champion import Champion
from src.interfaces.game import Game
from src.interfaces.strategies.champion_assignment import ChampionAssignmentStrategy

type Tags = tuple[str, ...]


class TagBasedChampionAssignment(ChampionAssignmentStrategy):
    def apply(self, game: Game) -> None:
        size = max(game.red.size, game.blue.size)
        champions = game.available_champions

        tag_count = self.generate_tag_count(champions)
        available_tags = self.filter_available_tags(tag_count)
        tags = self.select_tags(available_tags, count=size)

        filtered = self.filter_champions(champions, tags)
        red, blue = self.select_champions(filtered)

        for champ in red:
            game.red.add_champion(champ)

        for champ in blue:
            game.blue.add_champion(champ)

    def generate_tag_count(self, champions: Sequence[Champion]):
        tag_count: dict[Tags, int] = {}
        for champion in champions:
            tags = tuple(champion.tags)
            tag_count[tags] = tag_count.get(tags, 0) + 1

        return tag_count

    def filter_available_tags(self, tags: dict[Tags, int]) -> list[Tags]:
        available_tags = [tag for tag, count in tags.items() if count >= 2]

        return available_tags

    def select_tags(self, tags: list[Tags], count: int) -> list[Tags]:
        selected_tags = random.sample(tags, count)

        return selected_tags

    def filter_champions(
        self, champions: Sequence[Champion], tags: list[Tags]
    ) -> dict[Tags, Sequence[Champion]]:
        filtered: dict[Tags, Sequence[Champion]] = {}

        for tag in tags:
            tag_champions: Sequence[Champion] = []
            for champ in champions:
                if tuple(champ.tags) == tag:
                    tag_champions.append(champ)

            filtered[tag] = tag_champions

        return filtered

    def select_champions(
        self, champions: dict[Tags, Sequence[Champion]]
    ) -> tuple[Sequence[Champion], Sequence[Champion]]:
        team_champions = [
            random.sample(tag_champs, 2) for tag_champs in champions.values()
        ]

        champs = tuple(zip(*team_champions))

        return champs
