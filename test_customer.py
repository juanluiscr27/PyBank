""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from db.database_conn import ConnectionPool
from model.customer import Customer
from model.result import Return


# Database Configuration

config = {
    'user': 'pybank',
    'password': 'Lambton2022S',
    'host': 'localhost',
    'port': '3307',
    'database': 'pybank',
    'pool_name': 'pybank_conn_pool',
    'pool_size': 2
}

print("* Tests for Customer Model *")

""" Database Connection """
ConnectionPool.create_pool(**config)
result = Return()


# Test 1: View Customer
def test_view_customer():

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

    Customer.view_customer(active_customer, result)
