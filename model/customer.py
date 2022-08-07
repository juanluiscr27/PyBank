from dataclasses import dataclass
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
    def view_customer(customer_id, result):
        customer_accounts = []
        CustomerModel.view_customer(customer_id, customer_accounts, result)

        if result.code == "00":
            return customer_accounts

    @staticmethod
    def update_customer(active_customer, result):
        CustomerModel.update_customer(active_customer, result)

    @staticmethod
    def delete_customer(active_customer, result):
        delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if len(Customer.view_customer(active_customer.customer_id, result)) > 0:
            result.set_code("04")
            print(result.message)
        else:
            pass
            # CustomerModel.delete_customer(active_customer, delete_date, result)
