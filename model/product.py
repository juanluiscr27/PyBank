from dataclasses import dataclass, field

products = {
    1: ['Checking', 0.009, 10000, 20, -5000],
    2: ['Saving', 0.012, 6000, 10, 100],
    3: ['Investing', 0.05, 0, 0, 1000]
}


@dataclass
class Product:
    product_id: int
    product_type: str = field(init=False)
    interest_rate: float = field(init=False)
    amount_limit: float = field(init=False)
    quantity_limit: int = field(init=False)
    minimum_balance: float = field(init=False)

    def __post_init__(self):
        self.product_type = products[self.product_id][0]
        self.interest_rate = products[self.product_id][1]
        self.amount_limit = products[self.product_id][2]
        self.quantity_limit = products[self.product_id][3]
        self.minimum_balance = products[self.product_id][4]

    @staticmethod
    def get_account_type(acc_type_id: int):
        return products[acc_type_id][0]

    @staticmethod
    def get_minimum_balance(acc_type_id: int):
        return products[acc_type_id][4]
