from dataclasses import dataclass


products = {
    1: 'Checking',
    2: 'Saving',
    3: 'Inventing'
}


@dataclass
class Product:
    product_type: str
    interest_rate: float
    amount_limit: float
    quantity_limit: int
    minimum_balance: float

    @staticmethod
    def get_account_type(acc_type_id: int):
        return products[acc_type_id]
