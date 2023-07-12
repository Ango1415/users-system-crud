# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
"""
Script to config the log system of the program
"""
import logging as log


log.basicConfig(
    level='INFO',
    encoding='utf-8',
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I%M%S %p',
    handlers=[
        log.FileHandler('system_logs.log'),
        log.StreamHandler()
    ]
)
