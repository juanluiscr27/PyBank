""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from db.movement import get_transactions
from db.product import get_product_type
from model import util
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


# Test 2: Login Agent
def test_agent_login():
    print("* Tests for Agent Model *")
    active_agent = Agent()
    result = Return()
    active_agent.login("fboxe0", "ua8w6WmM", result)
    print(f"Agent {active_agent.first_name} logged in")


# Test 3: Search Customers
def test_search_customers():
    result = Return()
    customers = util.search_customer("Nan", result)
    print(customers)
    print("Len: ", len(customers))
    print("Code: ", result.code)


# Test 4: Search Accounts """
def test_search_accounts():
    result = Return()
    accounts = util.search_account("15", result)
    print("Len: ", len(accounts))
    print("Code: ", result.code)
    print(accounts)


# Test 5: Create Customer
def test_create_customer():
    result = Return()
    new_customer = Customer(
        customer_id=0,
        pin="5678",
        first_name="Hugo",
        last_name="Beltran",
        address="Bentley",
        phone_number="1234567890",
        email="hugo@email.com",
        creation_date=datetime.now(),
        agent_id='jmisk5'
    )
    util.create_customer(new_customer, result)


# Test 6: Create Account """
def test_open_account():
    result = Return()
    new_account = Account(
        acc_number="",
        acc_type_id=1,
        balance=0,
        transfer_amount=0,
        transfer_quantity=0,
        customer_id=12,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    util.open_account(new_account, result)


# Test 7: Search Products
def test_search_products():
    products = get_product_type()
    print(products)


# Test 8: Search Transactions
def test_get_transactions():
    transactions = get_transactions()
    print(transactions)
