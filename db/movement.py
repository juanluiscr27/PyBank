from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.result import Return


def get_transactions():
    conn = None
    transactions = {}
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT transaction_id, transaction_desc, fee, access_level " \
                    "  FROM transactions " \
                    "  ORDER BY transaction_id "
            cursor = conn.cursor()

            cursor.execute(query)
            for transaction_id, transaction_desc, fee, access_level in cursor:
                transactions[transaction_id] = [transaction_desc, fee, access_level]

            cursor.close()
        return transactions
    except errors.PoolError as pe:
        print(f"{pe.errno} Pool is exhausted due to many connection requests")
    except errors.Error as er:
        print(f'{er.errno}: {er.msg}')
    finally:
        if conn.is_connected():
            conn.close()


def create_transaction(active_movement, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "INSERT INTO movements  " \
                    "(source_account, destination_account, amount, prev_balance, " \
                    " new_balance, movement_date, transaction_id, agent_id) " \
                    "VALUES (%(source_account)s, %(destination_account)s, %(amount)s, " \
                    " %(prev_balance)s, %(new_balance)s, %(movement_date)s, " \
                    " %(transaction_id)s, %(agent_id)s)"
            cursor = conn.cursor()

            # Query scape parameters
            transaction_info = {
                'source_account': active_movement.source_account,
                'destination_account': active_movement.destination_account,
                'amount': active_movement.amount,
                'prev_balance': active_movement.previous_balance,
                'new_balance': active_movement.new_balance,
                'movement_date': active_movement.movement_date.strftime('%Y-%m-%d %H:%M:%S'),
                'transaction_id': active_movement.transaction_id,
                'agent_id': active_movement.agent_id
            }
            cursor.execute(query, transaction_info)
            cursor.close()

    except errors.PoolError as pe:
        print(f"{pe.errno} Pool is exhausted due to many connection requests")
    except errors.Error as er:
        result.set_code("99")
        conn.rollback()
        print(f'{er.errno}: {er.msg}')
    else:
        result.set_code("00")
        conn.commit()
    finally:
        if conn.is_connected():
            conn.close()
