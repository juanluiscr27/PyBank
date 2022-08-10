""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from model.account import Account
from model.result import Return
from model.movement import Movement
from model import util
from db import movement


# Test 1: View Account
def test_create_transaction():
    print("* Tests for Account Model *")
    acc_number = "371882838"
    result = Return()
    account = util.search_account(acc_number, result)
    print(account)
    active_movement = Movement(
        movement_id=0,
        source_account="",
        destination_account="371882838",
        amount=1000,
        previous_balance=0,
        new_balance=1000,
        movement_date=datetime.now(),
        transaction_id=7,
        agent_id="jmisk5"
    )
    movement.create_transaction(active_movement, result)


def test_deposit():
    result = Return()
    active_movement = Movement(
        movement_id=0,
        source_account="",
        destination_account="371882838",
        amount=5000,
        previous_balance=0,
        new_balance=0,
        movement_date=datetime.now(),
        transaction_id=7,
        agent_id="fboxe0"
    )

    active_account = Account(
        acc_number="371882838",
        acc_type_id=2,
        balance=0,
        transfer_amount=0,
        transfer_quantity=0,
        customer_id=11,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    util.deposit(active_movement, active_account, result)


def test_withdrawal():
    result = Return()
    active_movement = Movement(
        movement_id=0,
        source_account="371882838",
        destination_account="",
        amount=500,
        previous_balance=0,
        new_balance=0,
        movement_date=datetime.now(),
        transaction_id=8,
        agent_id="fboxe0"
    )

    active_account = Account(
        acc_number="371882838",
        acc_type_id=2,
        balance=5000,
        transfer_amount=0,
        transfer_quantity=0,
        customer_id=11,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    util.withdrawal(active_movement, active_account, result)


def test_transfer():
    result = Return()
    active_movement = Movement(
        movement_id=0,
        source_account="371882838",
        destination_account="350715313",
        amount=1200,
        previous_balance=0,
        new_balance=0,
        movement_date=datetime.now(),
        transaction_id=9,
        agent_id="fbampkin2"
    )

    active_account = Account(
        acc_number="371882838",
        acc_type_id=2,
        balance=4497.50,
        transfer_amount=502.50,
        transfer_quantity=1,
        customer_id=11,
        open_date=datetime.now(),
        agent_id="jmisk5"
    )
    util.transfer(active_movement, active_account, result)
