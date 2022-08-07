from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.movement import Movement
from model.result import Return


class AccountModel:

    @classmethod
    def view_acc_numbers(cls, account_numbers: list, result: Return):
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

    @classmethod
    def view_account(cls, acc_number, account_movements: list, result: Return):
        conn = None
        # Request a database connection from the pool
        try:
            conn = ConnectionPool.get_connection()

            if conn.is_connected():
                # print("Connection successful")
                query = "SELECT m.movement_id, m.source_account, m.destination_account, " \
                        " m.transaction_id, t.transaction_desc, m.amount, m.prev_balance, " \
                        " m.new_balance, m.movement_date " \
                        "	FROM movements m JOIN transactions t " \
                        " 	ON m.transaction_id = t.transaction_id " \
                        " WHERE m.source_account = %(acc_number)s " \
                        "	OR m.destination_account = %(acc_number)s " \
                        "	ORDER BY m.movement_date DESC "

                cursor = conn.cursor()

                # Query scape parameters
                customer_info = {
                    'acc_number': acc_number
                }

                cursor.execute(query, customer_info)
                row = cursor.fetchone()
                if cursor.rowcount > 0:
                    # Unpack row fields from the result
                    (movement_id, source_account, destination_account, transaction_id,
                     transaction_desc, amount, prev_balance, new_balance, movement_date) = row

                    bank_account = Movement(
                        movement_id=movement_id,
                        source_account=source_account,
                        destination_account=destination_account,
                        amount=amount,
                        previous_balance=prev_balance,
                        new_balance=new_balance,
                        movement_date=movement_date,
                        description=transaction_desc
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

    @classmethod
    def update_account(cls, bank_customer, result: Return):
        conn = None
        # Request a database connection from the pool
        try:
            conn = ConnectionPool.get_connection()

            if conn.is_connected():
                # print("Connection successful")
                query = "UPDATE customers SET " \
                        " pin = %(pin)s, first_name = %(first_name)s, last_name = %(last_name)s, " \
                        " address = %(address)s, phone_number = %(phone_number)s " \
                        " WHERE customer_id = %(customer_id)s "
                cursor = conn.cursor()

                # Query scape parameters
                customer_info = {
                    'customer_id': bank_customer.customer_id,
                    'pin': bank_customer.pin,
                    'first_name': bank_customer.first_name,
                    'last_name': bank_customer.last_name,
                    'address': bank_customer.address,
                    'phone_number': bank_customer.phone_number
                }
                cursor.execute(query, customer_info)
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

    @classmethod
    def delete_account(cls, bank_customer, delete_date: str, result: Return):
        conn = None
        # Request a database connection from the pool
        try:
            conn = ConnectionPool.get_connection()

            if conn.is_connected():
                # print("Connection successful")
                insert_query = "INSERT INTO customers_hist " \
                               " (customer_id, first_name, last_name, creation_date, " \
                               " delete_date, agent_id) " \
                               "VALUES (%(customer_id)s, %(first_name)s, %(last_name)s, " \
                               " %(creation_date)s, %(delete_date)s, %(agent_id)s) "

                cursor = conn.cursor()

                # Query scape parameters
                customer_info = {
                    'customer_id': bank_customer.customer_id,
                    'first_name': bank_customer.first_name,
                    'last_name': bank_customer.last_name,
                    'creation_date': bank_customer.creation_date,
                    'delete_date': delete_date,
                    'agent_id': bank_customer.agent_id
                }
                cursor.execute(insert_query, customer_info)

                delete_query = "DELETE FROM customers  " \
                               " WHERE customer_id = %s "

                cursor.execute(delete_query, (bank_customer.customer_id,))
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
