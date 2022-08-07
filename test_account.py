""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from model.customer import Customer
from model.result import Return


print("* Tests for Account Model *")


# Test 1: View Customer
def test_view_acc_num():
    result = Return()
    customer_id = 11

    customer_view = Customer.view_customer(customer_id, result)
    print(customer_view)


def test_view_account():
    result = Return()
    active_customer = Customer(
        customer_id=11,
        pin="1234",
        first_name="Juan Luis",
        last_name="Casanova",
        address="Bentley",
        phone_number="9876543210",
        email="juan@email.com",
        creation_date=datetime.now(),
        agent_id='jmisk5'
    )

    Customer.update_customer(active_customer, result)

