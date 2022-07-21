from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class Agent:
    username: str
    password: str
    first_name: str
    last_name: str
    position_id: int
