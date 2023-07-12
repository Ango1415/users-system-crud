# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
from cursor_pool import CursorPool
from logger_base import log
from user import User


class UserDAO:
    """
    Class DAO: Data Access Object
    Class to perform the transactions in the DB (CRUD functions)
    """

    _SELECT: str = 'SELECT * FROM users ORDER BY id_user'
    _INSERT: str = 'INSERT INTO users (username, password) VALUES(%s, %s)'
    _UPDATE: str = 'UPDATE users SET username = %s, password = %s WHERE id_user = %s'
    _DELETE: str = 'DELETE FROM users WHERE id_user = %s'

    @classmethod
    def select(cls):
        """
        Performs the selection queries in the DB
        :return: A list with the users records of the DB
        """
        users = []
        with CursorPool() as cursor:
            try:
                cursor.execute(cls._SELECT)
                rows = cursor.fetchall()

                for row in rows:
                    user = User(row[0], row[1], row[2])
                    users.append(user)
                log.info('List of successfully recovered users.')
            except Exception as e:
                log.error(f'An exception occurred: {e}')
        return users

    @classmethod
    def insert(cls, user: User):
        """
        Performs the insertion queries in the DB
        :param user: Object of the class who maps the user table in the DB, contains the info of the new user
        :return: number of records inserted
        """
        with CursorPool() as cursor:
            try:
                values = (user.username, user.password)
                cursor.execute(cls._INSERT, values)

                log.info('User successfully inserted.')
                log.info(f'User: {user}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'An exception occurred in the insertion: {e}')
                return 0

    @classmethod
    def update(cls, user: User):
        """
        Performs the 'update' queries in the DB
        :param user: Object of the class who maps the user table in the DB, contains the info of the new user
        :return: number of records updated
        """
        with CursorPool() as cursor:
            try:
                values = (user.username, user.password, user.id_user)
                cursor.execute(cls._UPDATE, values)

                log.info('User successfully updated.')
                log.info(f'User: {user}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'An exception occurred in the update: {e}')
                return 0

    @classmethod
    def delete(cls, user: User):
        """
        Performs the 'delete' queries in the DB
        :param user: Object of the class who maps the user table in the DB, contains the info of the new user
        :return: number of records deleted
        """
        with CursorPool() as cursor:
            try:
                values = (user.id_user,)
                cursor.execute(cls._DELETE, values)

                log.info('User successfully deleted.')
                log.info(f'User: {user}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'One exception occurred in the delete:: {e}')
                return None
