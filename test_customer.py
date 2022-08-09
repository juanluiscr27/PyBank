""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from model.customer import Customer
from model.result import Return
from model import util


print("* Tests for Customer Model *")


# Test 1: View Customer
def test_view_customer():
    result = Return()
    customer_id = 11

    customer_view = util.view_customer(customer_id, result)
    print(customer_view)


def test_update_customer():
    result = Return()
    active_customer = Customer(
        customer_id=11,
        pin="1234",
        first_name="Juan",
        last_name="Casanova",
        address="Bentley",
        phone_number="9876543210",
        email="juan@email.com",
        creation_date=datetime.now(),
        agent_id='jmisk5'
    )

    util.update_customer(active_customer, result)


def test_delete_customer():
    # TODO
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

    util.delete_customer(active_customer, result)
