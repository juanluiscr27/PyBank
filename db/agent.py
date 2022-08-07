from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.account import Account
from model.customer import Customer
from model.result import Return


class AgentModel:

    @classmethod
    def add_char_wildcard(cls, search_string: str):
        return f"%{search_string}%"

    @classmethod
    def validate_agent(cls, active_agent, input_username: str, result: Return):
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
        except errors.Error as er:
            conn.rollback()
            print(f'{er.errno}: {er.msg}')
        finally:
            if conn.is_connected():
                conn.close()
                # print("Connection closed")

    @classmethod
    def search_customer(cls, search_string: str, customers_result: list, result: Return):
        conn = None
        search_string = cls.add_char_wildcard(search_string)
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
        except errors.Error as er:
            conn.rollback()
            print(f'{er.errno}: {er.msg}')
        finally:
            if conn.is_connected():
                conn.close()

    @classmethod
    def search_account(cls, search_string: str, accont_result: list, result: Return):
        conn = None
        search_string = cls.add_char_wildcard(search_string)
        # Request a database connection from the pool
        try:
            conn = ConnectionPool.get_connection()

            if conn.is_connected():
                # print("Connection successful")
                query = "SELECT acc_number, acc_type, balance, transfer_amount, transfer_quantity, " \
                        "customer_id, open_date FROM accounts " \
                        "  WHERE LOWER(acc_number) LIKE %(search_string)s "
                cursor = conn.cursor()

                # Query scape parameters
                account_info = {
                    'search_string': search_string
                }

                cursor.execute(query, account_info)
                resul_set = cursor.fetchall()

                if cursor.rowcount > 0:
                    # Unpack row fields from the result
                    for (acc_number, acc_type, balance, transfer_amount, transfer_quantity,
                         customer_id, open_date) in resul_set:
                        bank_account = Account(
                            acc_number=acc_number,
                            acc_type=acc_type,
                            balance=balance,
                            transfer_amount=transfer_amount,
                            transfer_quantity=transfer_quantity,
                            customer_id=customer_id,
                            open_date=open_date
                        )
                        accont_result.append(bank_account)

                    result.set_code("00")
                else:
                    result.set_code("01")

                cursor.close()

        except errors.PoolError as pe:
            print(f"{pe.errno} Pool is exhausted due to many connection requests")
        except errors.Error as er:
            conn.rollback()
            print(f'{er.errno}: {er.msg}')
        finally:
            if conn.is_connected():
                conn.close()

    @classmethod
    def create_customer(cls, search_string: str, customers_result: list, result: Return):
        conn = None
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
        except errors.Error as er:
            conn.rollback()
            print(f'{er.errno}: {er.msg}')
        finally:
            if conn.is_connected():
                conn.close()