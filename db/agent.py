from mysql.connector import errors

from db.database_conn import ConnectionPool


class AgentModel:
    conn: None

    @classmethod
    def validate_agent(cls):
        conn = None
        # Request a database connection from the pool
        try:
            conn = ConnectionPool.get_connection()

            if conn.is_connected():
                # print("Connection successful")
                query = "SELECT * FROM agents WHERE username = %(username)s"
                cursor = conn.cursor()

                # Query scape parameters
                agent_username = {
                    'username': 'fbampkin2'
                }
                cursor.execute(query, agent_username)

                agents = cursor.fetchall()

                for customer in agents:
                    row = ""
                    for field in customer:
                        row += str(field) + "\t"
                    print(row)

                # Make sure data is committed to the database
                conn.commit()
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
