from dataclasses import dataclass

from db.agent import AgentModel


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
        return customers_result

    @staticmethod
    def search_account(search_string, result):
        """ Search bank accounts who match de provided search string.
            Return a list of accounts who satisfy the search criteria. """
        account_result = []
        AgentModel.search_account(search_string, account_result, result)
        return account_result

    @staticmethod
    def create_customer():
        """ Create a new bank customer """
        pass

    @staticmethod
    def open_customer():
        """ Create a new bank account """
        pass
