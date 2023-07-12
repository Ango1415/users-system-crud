# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
from logger_base import log
from psycopg2 import pool
import sys


class Connection:
    """
    Class to control the connection pool and the access to the postgres DB connections.
    A maximum of 5 connections are enabled in the pool.
    """
    _HOST: str = '127.0.0.1'
    _PORT: str = '5432'
    _DATABASE: str = 'test_db'
    _USER: str = 'postgres'
    _PASSWORD: str = 'admin'

    _MIN_CONN: int = 1
    _MAX_CONN: int = 5
    _pool = None

    @classmethod
    def obtain_pool(cls):
        """
        Establishes connection to the postgres DB and opens the connection pool.
        :return: Pool object to manage the connection pool.
        """
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONN,
                    cls._MAX_CONN,
                    host=cls._HOST,
                    port=cls._PORT,
                    database=cls._DATABASE,
                    user=cls._USER,
                    password=cls._PASSWORD
                )
                log.debug(f'Successful pool creation: {cls._pool}')
            except Exception as e:
                log.error(f'An exception occurred when obtaining the pool: {e}')
                sys.exit()
        return cls._pool

    @classmethod
    def obtain_connection(cls):
        """
        Gets a connection from the connection pool and returns it for use.
        :return: Connection object to perform transactions on the DB.
        """
        try:
            connection = cls.obtain_pool().getconn()
            log.debug(f'Connection successfully obtained from the pool: {connection}')
            return connection
        except Exception as e:
            log.error(f'An exception occurred while establishing pool connection: {e}')
            sys.exit()

    @classmethod
    def return_connection(cls, connection):
        """
        Return the connection to the connection pool, so that it can be released and used again in the future.
        :param connection: Object connection to be released.
        """
        try:
            cls.obtain_pool().putconn(connection)
            # conexion.putconn()    # This also could work
            log.debug(f'Connection successfully released and returned to connection pool: {connection}')
        except Exception as e:
            log.error(f'An exception occurred while releasing a connection: {e}')
            sys.exit()

    @classmethod
    def close_pool(cls):
        """
        Closes the connection pool object to completely close the connection between the program and the DB.
        """
        try:
            cls.obtain_pool().closeall()
            log.debug('Pool successfully closed')
        except Exception as e:
            log.error(f'An exception occurred when closing the connection pool: {e}')
            sys.exit()
