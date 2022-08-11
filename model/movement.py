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

    def copy(self):
        movement_copy = Movement(
            movement_id=self.movement_id,
            source_account=self.source_account,
            destination_account=self.destination_account,
            amount=self.amount,
            previous_balance=self.previous_balance,
            new_balance=self.new_balance,
            movement_date=self.movement_date,
            transaction_id=self.transaction_id,
            agent_id=self.agent_id
        )
        return movement_copy


class TransactionList:
    _transactions = None

    @classmethod
    def create_list(cls):
        if not cls._transactions:
            cls._transactions = get_transactions()

    @classmethod
    def get_list(cls):
        return cls._transactions
