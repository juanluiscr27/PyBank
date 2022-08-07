""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from datetime import datetime

import test_agent as ta
import test_customer as tc


def test():
    """ Test Agent Model """
    # ta.test_agent_login()
    # ta.test_search_customer()
    # ta.test_search_accounts()
    # ta.test_create_customer()
    # ta.test_search_products()
    # ta.search_create_account()

    """ Test Agent Model """
    tc.test_view_customer()


# Start the program
if __name__ == '__main__':
    test()
