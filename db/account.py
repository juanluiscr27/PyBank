from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.movement import Movement
from model.result import Return


def view_acc_numbers(account_numbers: list, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT ac.acc_number FROM accounts ac " \
                    "  LEFT OUTER JOIN accounts_hist ah " \
                    "  ON ac.acc_number  = ah.acc_number " \
                    "UNION " \
                    " SELECT ah.acc_number FROM accounts ac " \
                    " RIGHT OUTER JOIN accounts_hist ah " \
                    " ON ac.acc_number = ah.acc_number"
            cursor = conn.cursor()

            cursor.execute(query)
            resul_set = cursor.fetchall()

            if cursor.rowcount > 0:
                # Unpack row fields from the result
                for acc_number in resul_set:
                    account_numbers.append(acc_number)

                result.set_code("00")
            else:
                result.set_code("01")

            cursor.close()

    except errors.PoolError as pe:
        print(f"{pe.errno} Pool is exhausted due to many connection requests")
    except errors.Error as err:
        print(f'{err.errno}: {err.msg}')
    finally:
        if conn.is_connected():
            conn.close()


def view_account(acc_number, account_movements: list, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT movement_id, source_account, destination_account, " \
                    " transaction_id, amount, prev_balance, " \
                    " new_balance, movement_date, agent_id " \
                    "	FROM movements " \
                    " WHERE source_account = %(acc_number)s " \
                    "	OR destination_account = %(acc_number)s " \
                    "	ORDER BY movement_date DESC "

            cursor = conn.cursor()

            # Query scape parameters
            customer_info = {
                'acc_number': acc_number
            }

            cursor.execute(query, customer_info)
            resul_set = cursor.fetchall()
            if cursor.rowcount > 0:
                # Unpack row fields from the result
                for (movement_id, source_account, destination_account, transaction_id,
                     amount, prev_balance, new_balance, movement_date, agent_id) in resul_set:
                    bank_account = Movement(
                        movement_id=movement_id,
                        source_account=source_account,
                        destination_account=destination_account,
                        amount=amount,
                        previous_balance=prev_balance,
                        new_balance=new_balance,
                        movement_date=movement_date,
                        transaction_id=transaction_id,
                        agent_id=agent_id
                    )
                    account_movements.append(bank_account)

                result.set_code("00")

            cursor.close()

    except errors.PoolError as pe:
        print(f"{pe.errno} Pool is exhausted due to many connection requests")
    except errors.Error as er:
        result.set_code("99")
        print(f'{er.errno}: {er.msg}')
    finally:
        if conn.is_connected():
            conn.close()


def update_account(bank_account, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "UPDATE accounts SET " \
                    "  balance = %(balance)s, " \
                    "  transfer_amount = %(transfer_amount)s, " \
                    "  transfer_quantity = %(transfer_quantity)s " \
                    " WHERE acc_number = %(acc_number)s "
            cursor = conn.cursor()

            # Query scape parameters
            account_info = {
                'acc_number': bank_account.acc_number,
                'balance': bank_account.balance,
                'transfer_amount': bank_account.transfer_amount,
                'transfer_quantity': bank_account.transfer_quantity
            }
            cursor.execute(query, account_info)
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


def change_account_type(bank_account, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "UPDATE accounts SET " \
                    "  acc_type = %(acc_type)s " \
                    " WHERE acc_number = %(acc_number)s "
            cursor = conn.cursor()

            # Query scape parameters
            account_info = {
                'acc_number': bank_account.acc_number,
                'acc_type': bank_account.acc_type_id
            }
            cursor.execute(query, account_info)
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


def delete_account(bank_account, agent_id: str, delete_date: str, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            insert_query = "INSERT INTO accounts_hist " \
                           " (acc_number, acc_type, customer_id, open_date, close_date, agent_id) " \
                           "VALUES (%(acc_number)s, %(acc_type)s, %(customer_id)s, " \
                           " %(open_date)s, %(delete_date)s, %(agent_id)s) "

            cursor = conn.cursor()

            # Query scape parameters
            account_info = {
                'acc_number': bank_account.acc_number,
                'acc_type': bank_account.acc_type_id,
                'customer_id': bank_account.customer_id,
                'open_date': bank_account.open_date,
                'delete_date': delete_date,
                'agent_id': agent_id
            }
            cursor.execute(insert_query, account_info)

            delete_query = "DELETE FROM accounts  " \
                           " WHERE acc_number = %s "

            cursor.execute(delete_query, (bank_account.acc_number,))
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
