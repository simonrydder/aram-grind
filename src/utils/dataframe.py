from typing import Any, Sequence

from polars import DataFrame, List, Schema

from src.interfaces.champion import Champion


def champions_to_dataframe(champions: Sequence[Champion]) -> DataFrame:
    data: list[dict[str, Any]] = []
    for _, champ in enumerate(champions):
        state = champ.to_state()
        if state.tags is None:
            continue

        row: dict[str, Any] = {"name": state.name, "tags": list(state.tags)}

        data.append(row)

    schema = Schema(
        {
            "name": str,
            "tags": List(str),
        }
    )
    df = DataFrame(data, schema=schema)
    return df


def champion_to_dict(champion: Champion) -> dict[str, Any]:
    state = champion.to_state()
    dct = state.model_dump()
    return dct
