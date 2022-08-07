from mysql.connector import errors

from db.database_conn import ConnectionPool


class ProductModel:

    @classmethod
    def get_product_type(cls):
        conn = None
        products_type = {}
        # Request a database connection from the pool
        try:
            conn = ConnectionPool.get_connection()

            if conn.is_connected():
                # print("Connection successful")
                query = "SELECT product_id, product_type " \
                        "  FROM products " \
                        "  ORDER BY product_id "
                cursor = conn.cursor()

                cursor.execute(query)
                for product_id, product_type in cursor:
                    products_type[product_id] = product_type

                cursor.close()
            return products_type
        except errors.PoolError as pe:
            print(f"{pe.errno} Pool is exhausted due to many connection requests")
        except errors.Error as er:
            print(f'{er.errno}: {er.msg}')
        finally:
            if conn.is_connected():
                conn.close()
