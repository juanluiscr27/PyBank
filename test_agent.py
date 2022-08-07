""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from db.database_conn import ConnectionPool
from db.product import ProductModel
from model.account import Account
from model.agent import Agent
from model.customer import Customer
from model.result import Return

config = {
    'user': 'pybank',
    'password': 'Lambton2022S',
    'host': 'localhost',
    'port': '3307',
    'database': 'pybank',
    'pool_name': 'pybank_conn_pool',
    'pool_size': 1
}

print("* Tests for Agent Model *")


# Test 2: Login Agent
def test_agent_login():
    active_agent = Agent()
    result = Return()
    active_agent.login("fboxe0", "ua8w6WmM", result)
    print(f"Agent {active_agent.first_name} logged in")


# Test 3: Search Customers
def test_search_customers():
    result = Return()
    customers = Agent.search_customer("Nan", result)
    print("Len: ", len(customers))
    print("Code: ", result.code)


# Test 4: Search Accounts """
def test_search_accounts():
    result = Return()
    accounts = Agent.search_account("15", result)
    print("Len: ", len(accounts))
    print("Code: ", result.code)


# Test 5: Create Customer
def test_create_customer():
    result = Return()
    new_customer = Customer(
        customer_id=0,
        pin="1234",
        first_name="Juan",
        last_name="Casanova",
        address="Bentley",
        phone_number="9876543210",
        email="juan@email.com",
        creation_date=datetime.now(),
        agent_id='jmisk5'
    )
    Agent.create_customer(new_customer, result)


# Test 6: Search Products
def test_search_products():
    products = ProductModel.get_product_type()
    print(products)


# Test 7: Create Account """
def test_open_account():
    result = Return()
    new_account = Account(
        acc_number="",
        acc_type_id=1,
        balance=0,
        transfer_amount=0,
        transfer_quantity=0,
        customer_id=11,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    Agent.open_account(new_account, result)
