from typing import Any, Sequence

from polars import DataFrame

from src.interfaces.champion import Champion


def champions_to_dataframe(champions: Sequence[Champion]) -> DataFrame:
    data: list[dict[str, Any]] = []
    for _, champ in enumerate(champions):
        dct = champion_to_dict(champ)
        data.append(dct)

    return DataFrame(data)


def champion_to_dict(champion: Champion) -> dict[str, Any]:
    state = champion.to_state()
    dct = state.model_dump()
    return dct
