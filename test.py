""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""

from db.database_conn import ConnectionPool
from model.movement import TransactionList
from model.product import ProductList

# IMPORTS FOR TEST AGENT
import test_agent as ta

# IMPORTS FOR TEST CUSTOMER
import test_customer as tc

# IMPORTS FOR TEST ACCOUNT
import test_account as tac

# IMPORTS FOR TEST ACCOUNT
import test_movement as tm

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

""" Load Lookup Tables """
TransactionList.create_list()
ProductList.create_list()


def test():
    """ Test Agent Model """
    # ta.test_agent_login()
    # ta.test_search_customers()
    # ta.test_product_list()
    # ta.test_search_accounts()
    # ta.test_create_customer()
    # ta.test_open_account()
    # ta.test_search_products()
    # ta.test_get_transactions()

    """ Test Customer Model """
    # tc.test_view_customer()
    # tc.test_update_customer()
    # tc.test_delete_customer()

    """ Test Account Model """
    # tac.test_view_account()
    # tac.test_update_account()
    # tac.test_change_account_type()
    # tac.test_delete_account()

    """ Test Movement Model """
    # tm.test_transaction_list()
    # tm.test_create_transaction()
    # tm.test_deposit()
    # tm.test_withdrawal()
    # tm.test_transfer()


"""
INSERT INTO transactions 
  (transaction_id, transaction_desc, fee, access_level)
VALUES  (10, 'Fee', 0, 3);
"""

# Start the program
if __name__ == '__main__':
    test()
