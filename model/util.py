from datetime import datetime
from random import randint

from db import agent, account, customer, movement


""" AGENT FUNCTIONS """


def search_customer(search_string, result):
    """ Search bank customers who match de provided search string.
        Return a list of customers who satisfy the search criteria. """
    customers_result = []
    agent.search_customer(search_string, customers_result, result)
    if result.code == "00":
        return customers_result
    else:
        return None


def search_account(search_string, result):
    """ Search bank accounts who match de provided search string.
        Return a list of accounts who satisfy the search criteria. """
    account_result = []
    agent.search_account(search_string, account_result, result)
    if result.code == "00":
        return account_result
    else:
        return None


def create_customer(new_customer, result):
    """ Create a new bank customer """
    agent.create_customer(new_customer, result)


def open_account(new_account, result):
    """ Create a new bank account """
    acc_number = generate_acc_num(1, result)
    new_account.acc_number = acc_number
    print(new_account)
    agent.open_account(new_account, result)


""" ACCOUNT FUNCTIONS"""


def get_new_acc_num(acc_type_id: int):
    acc_number = randint(10000000, 99999999)
    if acc_type_id == 1:
        acc_number = acc_number + 300000000
    elif acc_type_id == 2:
        acc_number = acc_number + 600000000
    elif acc_type_id == 3:
        acc_number = acc_number + 900000000
    else:
        acc_number = acc_number + 100000000

    return str(acc_number)


def generate_acc_num(acc_type_id: int, result):
    """ Create a random bank account number different to the existing ones """
    account_numbers = []
    account.view_acc_numbers(account_numbers, result)

    acc_number = get_new_acc_num(acc_type_id)
    while acc_number in account_numbers:
        acc_number = get_new_acc_num(acc_type_id)

    return acc_number


def view_account(acc_number, result):
    """ Search bank account based on an account number """
    account_movements = []
    account.view_account(acc_number, account_movements, result)
    if result.code == "00":
        return account_movements


def update_account(bank_account, result):
    """ Update bank account based on an account number """
    account.update_account(bank_account, result)
    if result.code == "00":
        print(bank_account)


def change_account_type(bank_account, result):
    """ Update bank account based on an account number """
    account.change_account_type(bank_account, result)
    if result.code == "00":
        print(bank_account)


def delete_account(bank_account, result):
    """ Search bank account based on an account number """
    delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # TODO
    # account.delete_account(bank_account, delete_date, result)
    if result.code == "00":
        print(bank_account)


""" CUSTOMER FUNCTIONS """


def view_customer(customer_id, result):
    customer_accounts = []
    customer.view_customer(customer_id, customer_accounts, result)

    if result.code == "00":
        return customer_accounts


def update_customer(active_customer, result):
    customer.update_customer(active_customer, result)


def delete_customer(active_customer, result):
    delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if len(view_customer(active_customer.customer_id, result)) > 0:
        result.set_code("04")
        print(result.message)
    else:
        # TODO
        pass
        # customer.delete_customer(active_customer, delete_date, result)


""" MOVEMENTS FUNCTIONS """


def deposit(active_movement, active_account, active_agent, result):
    """ Deposit money into a bank account """
    # TODO
    active_movement.amount -= active_movement.get_transaction_fee
    active_movement.previous_balance = active_account.balance
    active_movement.new_balance = active_account.balance + active_movement.amount
    active_account.balance = active_movement.new_balance
    movement.create_transaction(active_movement, result)
    # account.update_account(bank_account, result)

    if result.code == "00":
        print("Deposit Successful")


def withdrawal(active_movement, active_account, active_agent, result):
    """ Withdraw money from a bank account """
    # TODO

    active_movement.amount -= active_movement.get_transaction_fee
    active_movement.previous_balance = active_account.balance
    active_movement.new_balance = active_account.balance + active_movement.amount
    if active_movement.new_balance < active_account.acc_type.minimum_balance:
        result.set_code("06")

    elif result.code == "00":
        active_account.transfer_mount += active_movement.amount
        active_account.transfer_quantity = active_account.transfer_quantity + 1
        active_account.balance = active_movement.new_balance

        # movement.create_transaction(active_movement, result)
        # account.update_account(bank_account, result)
    if result.code == "00":
        print("Withdrawal Successful")


def transfer(active_movement, active_account, destination_account, active_agent, result):
    """ Transfer money from a bank account to another account """
    # TODO
    active_product = active_account.acc_type
    agent.search_account(destination_account, active_agent, result)
    active_movement.destination_account = destination_account.acc_number

    active_movement.amount -= active_movement.get_transaction_fee
    active_movement.previous_balance = active_account.balance
    active_movement.new_balance = active_account.balance + active_movement.amount
    if active_movement.new_balance < active_product.minimum_balance:
        result.set_code("06")
    elif active_account.transfer_quantity > active_product.minimum_balance:
        result.set_code("07")
    elif active_account.transfer_quantity > active_product.amount_limit:
        result.set_code("07")

    elif active_account.transfer_amount + active_movement.amount > active_product.amount_limit:
        result.set_code("08")
    elif result.code == "00":
        active_account.transfer_mount += active_movement.amount
        active_account.transfer_quantity = active_account.transfer_quantity + 1
        active_account.balance = active_movement.new_balance
        # movement.create_transaction(active_movement, result)
        account.update_account(active_account, result)

    if result.code == "00":
        print("Transfer Successful")
