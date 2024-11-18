from fastapi.testclient import TestClient


def skip_rounds(client: TestClient, jumps: int, winner: str) -> TestClient:
    for _ in range(jumps):
        client.get("/game/new_round")
        client.post("/game/round_winner", json={"team": winner})

    return client
