# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
"""
Main menu of the program
"""

from user_dao import UserDAO, User
from logger_base import log


log.info('Starting the User Management Program')
while True:
    print('USER MANAGEMENT SYSTEM'.center(50, '*'))
    print('''What do you want to do?
     1) List users
     2) Add users
     3) Update users
     4) Delete users
     5) Exit''')
    try:
        value = int(input('SELECTION: '))
        if 1 < value > 5:
            raise Exception(f'Value {value} out of range.')
    except Exception as e:
        log.error(f'An exception occurred: {e} , {type(e)}')
        continue

    if value == 1:
        log.info('List users')
        try:
            usuarios = UserDAO.select()
            for usuario in usuarios:
                log.info(usuario)

            input(' Press the ENTER key to continue...\n')
            continue
        except Exception as e:
            log.error(f'An exception occurred: {e}')
            continue

    elif value == 2:
        try:
            log.info('Add users')
            entrada = input('Enter the username and password values separated by commas (username,password): ')
            valores = tuple(entrada.split(','))
            usuario = User(username=valores[0], password=valores[1])
            count = UserDAO.insert(usuario)

            log.info(f'User(s) added: {count}')
            input(' Press the ENTER key to continue...\n')
            continue
        except Exception as e:
            log.error(f'An exception occurred: {e}')
            continue

    elif value == 3:
        try:
            log.info('Update users')
            entrada = input('Enter the id of the user to update and the values for username and password, '
                            'respectively, separated by commas (id,name,pass): ')
            valores = tuple(entrada.split(','))
            usuario = User(id_usuario=int(valores[0]), username=valores[1], password=valores[2])
            count = UserDAO.update(usuario)

            log.info(f'Updated user(s): {count}')
            input(' Press the ENTER key to continue...\n')
            continue
        except Exception as e:
            log.error(f'An exception occurred: {e}')
            continue

    elif value == 4:
        try:
            log.info('Delete users')
            entrada = input('Enter the user id of the user to be deleted:')
            usuario = User(id_usuario=int(entrada))
            count = UserDAO.delete(usuario)

            log.info(f'User(s) deleted: {count}')
            input(' Press the ENTER key to continue...\n')
            continue
        except Exception as e:
            log.error(f'An exception occurred: {e}')
            continue

    elif value == 5:
        print('End of the program'.center(50, '*'))
        log.info('Finalising the user management program')
        break
