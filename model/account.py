from dataclasses import dataclass, field
from datetime import date

from db.product import ProductModel


def get_account_type(acc_type_id: int):
	products = ProductModel.get_product_type()
	return products[acc_type_id]


@dataclass(kw_only=True, slots=True)
class Account:
	acc_number: str
	acc_type_id: int
	balance: float
	transfer_amount: float
	transfer_quantity: int
	customer_id: int
	open_date: date
	agent_id: str
	acc_type: str = field(init=False)

	def __post_init__(self):
		self.acc_type = get_account_type(self.acc_type_id)

	@staticmethod
	def view_account():
		""" Search bank account based on an account id """
		pass

