from src.interfaces.player import Player, PlayerDict


class StandardPlayer(Player):
    def __init__(self, name: str = "") -> None:
        super().__init__()

        self._name: str = name
        self._score: int = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, new_score: int) -> None:
        if new_score < 0:
            raise ValueError("Score must be a non-negative integer")

        self._score = new_score

    def to_dict(self) -> PlayerDict:
        return PlayerDict(name=self._name, score=self._score)
