from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True, slots=True)
class Movement:
    movement_id: int
    source_account: str
    destination_account: str
    amount: str
    previous_balance: str
    new_balance: str
    movement_date: datetime
    description: str
