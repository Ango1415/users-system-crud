# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
class User:
    """
    Class to map the 'user' table in the DB
    """

    def __init__(self, id_usuario: int = None, username: str = None, password: str = None):
        """
        Constructor of the class
        :param id_usuario: User's identifier (maps the 'id_user' column)
        :param username: User's name (maps the 'id_user' column )
        :param password: User's password (maps the 'password' column)
        """
        self._id_user = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'''
            Id user : {self._id_user}
            Username: {self._username}
            Password: {self._password}
        '''

    @property
    def id_user(self):
        return self._id_user

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @id_user.setter
    def id_user(self, id_user: int):
        self._id_user = id_user

    @username.setter
    def username(self, username: str):
        self._username = username

    @password.setter
    def password(self, password: str):
        self._password = password
