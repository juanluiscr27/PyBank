""" Term Project - PyBank
CSD 4523 - Python II
CSAM   Group 02   2022S
"""
from db.database_conn import ConnectionPool
import tkinter as tk

from model.agent import Agent
from ui.gui import *


def main():
    """ Application main method """
    # Database Configuration
    config = {
        'user': 'pybank',
        'password': 'Lambton2022S',
        'host': 'localhost',
        'port': '3306',
        'database': 'pybank',
        'pool_name': 'pybank_conn_pool',
        'pool_size': 1
    }

    print("* Welcome to PyBank *")

    ConnectionPool.create_pool(**config)

    active_agent = Agent()
    window = tk.Tk()
    result = Return();

    agent_login(window, active_agent, result)
    #if return == 0:
        #open search window
    window.mainloop()


# Start the program
if __name__ == '__main__':
    main()
