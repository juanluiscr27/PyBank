from dataclasses import dataclass, field
from datetime import datetime

from db.customer import CustomerModel


@dataclass(kw_only=True, slots=True)
class Customer:
    customer_id: int
    pin: str
    first_name: str
    last_name: str
    address: str
    phone_number: str
    email: str
    creation_date: datetime
    agent_id: str

    @staticmethod
    def view_customer(active_customer, result):
        customer_accounts = []
        CustomerModel.view_customer(active_customer, customer_accounts, result)
        print(result.code)
        if result.code == "00":
            print(customer_accounts)
