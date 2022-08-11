from dataclasses import dataclass, field
from datetime import datetime

from db.movement import get_transactions


@dataclass(kw_only=True, slots=True)
class Movement:
    transaction_id: int
    movement_id: int = 0
    source_account: str = ""
    destination_account: str = ""
    amount: float = 0
    previous_balance: float = 0
    new_balance: float = 0
    movement_date: datetime = None
    description: str = field(init=False)
    agent_id: str = ""

    def __post_init__(self):
        self.description = TransactionList.get_list()[self.transaction_id][0]

    def get_transaction_fee(self):
        return TransactionList.get_list()[self.transaction_id][1]


class TransactionList:
    _transactions = None

    @classmethod
    def create_list(cls):
        if not cls._transactions:
            cls._transactions = get_transactions()

    @classmethod
    def get_list(cls):
        return cls._transactions
