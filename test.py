""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

from db.database_conn import ConnectionPool
# IMPORTS FOR TEST AGENT
# import test_agent as ta

# IMPORTS FOR TEST CUSTOMER
import test_customer as tc


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

""" Test 1: Connection Pool"""
# conn_pool = ConnectionPool()
# conn_pool.create_pool(**config)
# conn = conn_pool.get_connection()

""" Database Connection """
ConnectionPool.create_pool(**config)


def test():
    """ Test Agent Model """
    # ta.test_agent_login()
    # ta.test_search_customers()
    # ta.test_search_accounts()
    # ta.test_create_customer()
    # ta.test_search_products()
    # ta.test_open_account()

    """ Test Agent Model """
    # tc.test_view_customer()
    # tc.test_update_customer()
    tc.test_delete_customer()


# Start the program
if __name__ == '__main__':
    test()
