""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from db.database_conn import ConnectionPool
from model.agent import Agent
from model.result import Return


def test():
    """ Application main method """
    # Database Configuration

    config = {
        'user': 'pybank',
        'password': 'Lambton2022S',
        'host': 'localhost',
        'port': '3307',
        'database': 'pybank',
        'pool_name': 'pybank_conn_pool',
        'pool_size': 1
    }

    print("* PyBank Project Test *")
    """ Test 1: Connection Pool"""
    # conn_pool = ConnectionPool()
    # conn_pool.create_pool(**config)
    # conn = conn_pool.get_connection()

    ConnectionPool.create_pool(**config)
    active_agent = Agent()
    result = Return()

    """ Test 2: Login Agent """
    # active_agent.login("fboxe0", "ua8w6WmM", result)
    # print(f"Agent {active_agent.first_name} logged in")

    """ Test 3: Search Customers """
    # customers = Agent.search_customer("Nan", result)
    # print("Len: ", len(customers))
    # print("Code: ", result.code)

    """ Test 4: Search Accounts """
    accounts = Agent.search_account("15", result)
    print("Len: ", len(accounts))
    print("Code: ", result.code)


# Start the program
if __name__ == '__main__':
    test()
