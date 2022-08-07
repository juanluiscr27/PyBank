from dataclasses import dataclass, field
from datetime import date
from random import randint

from db.account import AccountModel
from db.product import ProductModel


def get_new_acc_num(acc_type_id: int):
	acc_number = randint(10000000, 99999999)
	if acc_type_id == 1:
		acc_number = acc_number + 300000000
	elif acc_type_id == 2:
		acc_number = acc_number + 600000000
	elif acc_type_id == 3:
		acc_number = acc_number + 900000000
	else:
		acc_number = acc_number + 100000000

	return str(acc_number)


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

	@staticmethod
	def generate_acc_num(acc_type_id: int, result):
		account_numbers = []
		AccountModel.view_acc_numbers(account_numbers, result)

		acc_number = get_new_acc_num(acc_type_id)
		while acc_number in account_numbers:
			acc_number = get_new_acc_num(acc_type_id)

		return acc_number
