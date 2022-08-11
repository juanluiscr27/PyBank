""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from db.database_conn import ConnectionPool
from model.movement import TransactionList
from model.product import ProductList
from ui.gui import *


def main():
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

    print("* Welcome to PyBank *")

    """ Database Connection """
    ConnectionPool.create_pool(**config)

    """ Load Lookup Tables """
    TransactionList.create_list()
    ProductList.create_list()

    main_window = GUI()

    main_window.agent_login()

    main_window.start_gui()


# Start the program
if __name__ == '__main__':
    main()
