""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from model import util
from model.account import Account
from model.result import Return


print("* Tests for Account Model *")


# Test 1: View Account
def test_view_account():
    result = Return()
    acc_number = "937850261"
    account_view = util.view_account(acc_number, result)
    print(account_view)


def test_update_account():
    result = Return()
    customer_account = Account(
        acc_number="350715313",
        acc_type_id=1,
        balance=0,
        transfer_amount=0,
        transfer_quantity=0,
        customer_id=12,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    util.update_account(customer_account, result)


def test_change_account_type():
    result = Return()
    customer_account = Account(
        acc_number="350715313",
        acc_type_id=3,
        balance=0,
        transfer_amount=0,
        transfer_quantity=0,
        customer_id=12,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    util.change_account_type(customer_account, result)


def test_delete_account():
    result = Return()
    # TODO
