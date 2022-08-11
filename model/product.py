from dataclasses import dataclass, field
from db.product import get_product_type


@dataclass
class Product:
    product_id: int
    product_type: str = field(init=False)
    interest_rate: float = field(init=False)
    amount_limit: float = field(init=False)
    quantity_limit: int = field(init=False)
    minimum_balance: float = field(init=False)

    def __post_init__(self):
        self.product_type = ProductList.get_list()[self.product_id][0]
        self.interest_rate = ProductList.get_list()[self.product_id][1]
        self.amount_limit = ProductList.get_list()[self.product_id][2]
        self.quantity_limit = ProductList.get_list()[self.product_id][3]
        self.minimum_balance = ProductList.get_list()[self.product_id][4]

    @staticmethod
    def get_account_type(acc_type_id: int):
        return ProductList.get_list()[acc_type_id][0]

    @staticmethod
    def get_minimum_balance(acc_type_id: int):
        return ProductList.get_list()[acc_type_id][4]


class ProductList:
    _products = None

    @classmethod
    def create_list(cls):
        if not cls._products:
            cls._products = get_product_type()

    @classmethod
    def get_list(cls):
        return cls._products
