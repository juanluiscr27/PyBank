from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.account import Account
from model.result import Return


def view_customer(customer_id, customer_accounts: list, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT a.acc_number, a.acc_type, p.product_type, a.balance, a.transfer_amount, " \
                    " a.transfer_quantity, a.customer_id, a.open_date,	a.agent_id " \
                    " FROM accounts a JOIN products p ON a.acc_type = p.product_id " \
                    " WHERE a.customer_id = %(customer_id)s"
            cursor = conn.cursor()

            # Query scape parameters
            customer_info = {
                'customer_id': customer_id
            }

            cursor.execute(query, customer_info)
            result_set = cursor.fetchall()
            if cursor.rowcount > 0:
                # Unpack row fields from the result
                for (acc_number, acc_type, product_type, balance, transfer_amount, transfer_quantity,
                     customer_id, open_date, agent_id) in result_set:
                    bank_account = Account(
                        acc_number=acc_number,
                        acc_type_id=acc_type,
                        balance=balance,
                        transfer_amount=transfer_amount,
                        transfer_quantity=transfer_quantity,
                        customer_id=customer_id,
                        open_date=open_date,
                        agent_id=agent_id
                    )
                    customer_accounts.append(bank_account)

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


def update_customer(bank_customer, result: Return):
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


def delete_customer(bank_customer, delete_date: str, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            insert_query = "INSERT INTO customers_hist " \
                           " (customer_id, first_name, last_name, creation_date, delete_date, " \
                           " agent_id) " \
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
