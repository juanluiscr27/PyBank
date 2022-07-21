from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class Movement:
    movement_id: int
    source_account: str
    destination_account: str
    amount: str
    previous_balance: str
    new_balance: str
    movement_date: str
    description: str
