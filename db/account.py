from datetime import date


class AccountModel:
	acc_number: str
	acc_type: str
	balance: float
	transfer_amount: float
	transfer_quantity: int
	customer_id: int
	open_date: date
