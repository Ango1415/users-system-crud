# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
from logger_base import log
from connection import Connection
import sys


class CursorPool:
    """
    Context Manager Class:
    Class to define the cursor object of the connection established with the DB.
    It will help us to manage the transactions made from our program to the DB.
    """
    def __init__(self):
        """
        Constructor of the class
        """
        self._conn = None       # Connection established between the DB and the program
        self._cursor = None     # Cursor object, will help us to carry out transactions

    def __enter__(self):
        """
        Method to open the cursor of the actual connection
        :return: Cursor object
        """
        try:
            log.debug('Start method: with __enter__')
            self._conn = Connection.obtain_connection()
            self._cursor = self._conn.cursor()
            return self._cursor
        except Exception as e:
            log.error(f'An exception occurred in the __enter__ method: {e}')
            sys.exit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Method to close the cursor
        :param exc_type: Type of exception
        :param exc_val: Value of the exception
        :param exc_tb: Traceback of the exception
        """
        try:
            log.debug('Start method: with __exit__')
            if exc_val:
                self._conn.rollback()
                log.error(f'An exception occurred when the changes persisted: {exc_val}, {exc_type}, {exc_tb}')
                log.error('Rollback on changes made...')
            else:
                self._conn.commit()
                log.debug('Commit on changes made...')

            self._cursor.close()
            Connection.return_connection(self._conn)
        except Exception as e:
            log.error(f'An error occurred (__exit__): {e}')
