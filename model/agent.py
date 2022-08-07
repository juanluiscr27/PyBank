from dataclasses import dataclass

from db.agent import AgentModel
from model.account import Account


@dataclass(kw_only=True, slots=True)
class Agent:
    username: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    position_id: int = ""

    def login(self, username, password, result):
        """ Search for the bank agent and validate his credentials """
        AgentModel.validate_agent(self, username, result)

        if result.code == "00":
            if self.password != password:
                result.set_code("02")

    @staticmethod
    def search_customer(search_string, result):
        """ Search bank customers who match de provided search string.
            Return a list of customers who satisfy the search criteria. """
        customers_result = []
        AgentModel.search_customer(search_string, customers_result, result)
        if result.code == "00":
            return customers_result
        else:
            return None

    @staticmethod
    def search_account(search_string, result):
        """ Search bank accounts who match de provided search string.
            Return a list of accounts who satisfy the search criteria. """
        account_result = []
        AgentModel.search_account(search_string, account_result, result)
        if result.code == "00":
            return account_result
        else:
            return None

    @staticmethod
    def create_customer(new_customer, result):
        """ Create a new bank customer """
        AgentModel.create_customer(new_customer, result)

    @staticmethod
    def open_account(new_account, result):
        """ Create a new bank account """
        acc_number = Account.generate_acc_num(1, result)
        new_account.acc_number = acc_number
        print(new_account)
        AgentModel.open_account(new_account, result)
