""" Connection pool class """

from mysql.connector import pooling, errors


class ConnectionPool:
    """
    Create a pool of connection to a MySQL database with the create pool method.
    Return PooledMySQLConnection  through the get connection method.
    """

    _conn_pool = None
    _conn = None

    @classmethod
    def create_pool(cls, **kwargs: dict) -> None:
        """
        Create a connection pool, after created, the request of connecting
        MySQL could get a connection from this pool instead of request to
        create a connection.

        :param, kwargs: a key word argument with the value of the pool parameters
        """
        print('Creating connection pool...')
        try:
            cls._conn_pool = pooling.MySQLConnectionPool(
                pool_name=kwargs['pool_name'],
                pool_size=kwargs['pool_size'],
                host=kwargs['host'],
                port=kwargs['port'],
                user=kwargs['user'],
                password=kwargs['password'],
                database=kwargs['database']
            )

            print('Connection pool created')
        except errors.Error as e:
            print(f'{e.errno}: {e.msg}')
            print('Connection pool could not be created')

    @classmethod
    def get_connection(cls) -> pooling.PooledMySQLConnection:

        try:
            # fetch a connection from the pool
            cls._conn = cls._conn_pool.get_connection()
            print('Connected to the database')

        except errors.PoolError as pe:
            # connection pool exhausted
            print(f'{pe.errno}: {pe.msg}')
            cls._conn.close()
            print('Database connection closed')

        return cls._conn
