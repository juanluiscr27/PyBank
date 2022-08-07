
from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.account import Account
from model.result import Return


class CustomerModel:
    conn: None

    @classmethod
    def view_customer(cls, bank_customer, customer_accounts: list, result: Return):
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
                    'customer_id': bank_customer.customer_id
                }

                cursor.execute(query, customer_info)
                resul_set = cursor.fetchone()
                if cursor.rowcount > 0:

                    # Unpack row fields from the result
                    for (acc_number, acc_type, product_type, balance, transfer_amount, transfer_quantity,
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
