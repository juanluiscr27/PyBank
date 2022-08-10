from dataclasses import dataclass, field
from datetime import datetime


transactions = {
    1: ['Create customer', 0, 3],
    2: ['Update customer', 0, 2],
    3: ['Delete customer', 0, 1],
    4: ['Opening account', 0, 3],
    5: ['Change account type', 4, 3],
    6: ['Close account', 0, 1],
    7: ['Deposit', 0, 3],
    8: ['Withdrawal', 2.50, 2],
    9: ['Funds transfer', 3.50, 2]
}


@dataclass(kw_only=True, slots=True)
class Movement:
    transaction_id: int
    movement_id: int = 0
    source_account: str = ""
    destination_account: str = ""
    amount: int = 0
    previous_balance: int = 0
    new_balance: int = 0
    movement_date: datetime = None
    description: str = field(init=False)
    agent_id: str = ""

    def __post_init__(self):
        self.description = transactions[self.transaction_id][0]

    def get_transaction_fee(self):
        return transactions[self.transaction_id][1]
