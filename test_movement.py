""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from model.result import Return
from model.account import Account
from model import util
from db import movement


print("* Tests for Account Model *")


# Test 1: View Account
def test_create_transaction():
    # TODO
    acc_number = "371882838"
    result = Return()
    account = util.search_account(acc_number, result)
    print(account)
    # active_movement = Movement(
    #     movement_id=0,
    #     source_account="",
    #     destination_account="",
    #     amount=0,
    #     previous_balance=0,
    #     new_balance=0,
    #     movement_date=datetime.now(),
    #     transaction_id=1,
    #     agent_id="jmisk5"
    # )
    # movement.create_transaction(active_movement, result)

