from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.result import Return


def create_transaction(active_movement, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "INSERT INTO movements  " \
                    "(source_account, destination_account, amount, prev_balance, " \
                    " new_balance, creation_date, transaction_id, agent_id) " \
                    "VALUES (%(source_account)s, %(destination_account)s, %(amount)s, " \
                    " %(prev_balance)s, %(new_balance)s, %(creation_date)s, " \
                    " %(transaction_id)s, %(agent_id)s)"
            cursor = conn.cursor()

            # Query scape parameters
            transaction_info = {
                'source_account': active_movement.source_account,
                'destination_account': active_movement.destination_account,
                'amount': active_movement.amount,
                'prev_balance': active_movement.prev_balance,
                'new_balance': active_movement.new_balance,
                'creation_date': active_movement.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
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
