from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.account import Account
from model.customer import Customer
from model.result import Return


def add_char_wildcard(search_string: str):
    return f"%{search_string}%"


def validate_agent(active_agent, input_username: str, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT username, password, first_name, last_name, position_id" \
                    "  FROM agents " \
                    "  WHERE username = %(username)s"
            cursor = conn.cursor()

            # Query scape parameters
            agent_username = {
                'username': input_username
            }

            cursor.execute(query, agent_username)
            row = cursor.fetchone()
            if cursor.rowcount > 0:

                # Unpack row fields from the result
                (username, password, first_name, last_name, position_id) = row

                active_agent.username = username
                active_agent.password = password
                active_agent.first_name = first_name
                active_agent.last_name = last_name
                active_agent.position_id = position_id

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
            # print("Connection closed")


def search_customer(search_string: str, customers_result: list, result: Return):
    conn = None
    search_string = add_char_wildcard(search_string)
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT customer_id, pin, first_name, last_name, address, phone_number, " \
                    "email, creation_date, agent_id FROM customers " \
                    "  WHERE LOWER(first_name) LIKE %(search_string)s " \
                    "  OR LOWER(last_name) LIKE %(search_string)s " \
                    "  OR LOWER(address) LIKE %(search_string)s " \
                    "  OR LOWER(phone_number) LIKE %(search_string)s " \
                    "  OR LOWER(email) LIKE %(search_string)s"
            cursor = conn.cursor()

            # Query scape parameters
            customer_info = {
                'search_string': search_string
            }

            cursor.execute(query, customer_info)
            resul_set = cursor.fetchall()

            if cursor.rowcount > 0:
                # Unpack row fields from the result
                for (customer_id, pin, first_name, last_name, address,
                     phone_number, email, creation_date, agent_id) in resul_set:
                    bank_customer = Customer(
                        customer_id=customer_id,
                        pin=pin,
                        first_name=first_name,
                        last_name=last_name,
                        address=address,
                        phone_number=phone_number,
                        email=email,
                        creation_date=creation_date,
                        agent_id=agent_id
                    )
                    customers_result.append(bank_customer)

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


def search_account(search_string: str, account_result: list, result: Return):
    conn = None
    search_string = add_char_wildcard(search_string)
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "SELECT acc_number, acc_type, balance, transfer_amount, transfer_quantity, " \
                    "customer_id, open_date, agent_id FROM accounts " \
                    "  WHERE acc_number LIKE %(search_string)s "
            cursor = conn.cursor(buffered=True)

            cust_query = "SELECT pin, first_name, last_name, address, phone_number, " \
                         " email, creation_date, agent_id FROM customers " \
                         " WHERE customer_id = %s"
            cust_cursor = conn.cursor(buffered=True)
            # Query scape parameters
            account_info = {
                'search_string': search_string
            }

            cursor.execute(query, account_info)
            resul_set = cursor.fetchall()

            if cursor.rowcount > 0:
                # Unpack row fields from the result
                for (acc_number, acc_type, balance, transfer_amount, transfer_quantity,
                     customer_id, open_date, agent_id) in resul_set:
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
                    cust_cursor.execute(cust_query, (customer_id,))

                    for (pin, first_name, last_name, address, phone_number, email, creation_date,
                         cust_agent_id) in cust_cursor:
                        bank_customer = Customer(
                            customer_id=customer_id,
                            pin=pin,
                            first_name=first_name,
                            last_name=last_name,
                            address=address,
                            phone_number=phone_number,
                            email=email,
                            creation_date=creation_date,
                            agent_id=cust_agent_id
                        )
                        bank_account.customer = bank_customer
                    account_result.append(bank_account)

                result.set_code("00")
            else:
                result.set_code("12")

            cursor.close()

    except errors.PoolError as pe:
        print(f"{pe.errno} Pool is exhausted due to many connection requests")
    except errors.Error as err:
        print(f'{err.errno}: {err.msg}')
    finally:
        if conn.is_connected():
            conn.close()


def create_customer(new_customer: Customer, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "INSERT INTO customers " \
                    "(pin, first_name, last_name, address, phone_number," \
                    " email, creation_date, agent_id) " \
                    "VALUES (%(pin)s, %(first_name)s, %(last_name)s, %(address)s, " \
                    "  %(phone_number)s, %(email)s, %(creation_date)s, %(agent_id)s)"
            cursor = conn.cursor()

            # Query scape parameters
            customer_info = {
                'pin': new_customer.pin,
                'first_name': new_customer.first_name,
                'last_name': new_customer.last_name,
                'address': new_customer.address,
                'phone_number': new_customer.phone_number,
                'email': new_customer.email,
                'creation_date': new_customer.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
                'agent_id': new_customer.agent_id
            }
            cursor.execute(query, customer_info)
            new_customer.customer_id = cursor.lastrowid
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


def open_account(new_account: Account, result: Return):
    conn = None
    # Request a database connection from the pool
    try:
        conn = ConnectionPool.get_connection()

        if conn.is_connected():
            # print("Connection successful")
            query = "INSERT INTO accounts" \
                    "  (acc_number, acc_type, balance, transfer_amount, " \
                    "  transfer_quantity, customer_id, open_date, agent_id) " \
                    "VALUES (%(acc_number)s, %(acc_type)s, %(balance)s, %(transfer_amount)s, " \
                    "  %(transfer_quantity)s, %(customer_id)s, %(open_date)s, %(agent_id)s)"
            cursor = conn.cursor()

            # Query scape parameters
            account_info = {
                'acc_number': new_account.acc_number,
                'acc_type': new_account.acc_type_id,
                'balance': new_account.balance,
                'transfer_amount': new_account.transfer_amount,
                'transfer_quantity': new_account.transfer_quantity,
                'customer_id': new_account.customer_id,
                'open_date': new_account.open_date,
                'agent_id': new_account.agent_id
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
