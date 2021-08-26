"""
postgres_connect.py

These will be scripts to connect to the postgres server
"""

import psycopg2
import pandas as pd
from postgres_config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




'''
The main function used to test functions from this python script
'''
def main():
    connect()


if __name__ == '__main__':
    main()