
from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.result import Return


class CustomerModel:
    conn: None

    @classmethod
    def create_customer(cls, active_agent, input_username: str, result: Return):
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
