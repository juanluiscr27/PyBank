from dataclasses import dataclass
from datetime import date


@dataclass(kw_only=True, slots=True)
class Account:
	acc_number: str
	acc_type: str
	balance: float
	transfer_amount: float
	transfer_quantity: int
	customer_id: int
	open_date: date

	@staticmethod
	def view_account():
		""" Search bank account based on an account id """
		pass

