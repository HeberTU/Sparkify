# -- coding: utf-8 --
"""This script create the Sparkify database and all its tables. """
from typing import Tuple
import psycopg2
from sql_queries import create_table_queries, drop_table_queries
import argparse
from psycopg2.extensions import cursor as Cursor
from psycopg2.extensions import connection as Connection


def create_database(
        user_name: str,
        password: str
) -> Tuple[Cursor, Connection]:
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    try:
        conn = psycopg2.connect(
            f"host=127.0.0.1 dbname=postgres user={user_name} "
            f"password={password}")

        conn.set_session(autocommit=True)

        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS sparkifydb")
            cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' "
                        "TEMPLATE template0"
                        )
    finally:
        if conn:
            conn.close()


    # connect to sparkify database
    conn = psycopg2.connect(
        f"host=127.0.0.1 dbname=sparkifydb user={user_name} "
        f"password={password}"
    )
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main(user_name: str, password: str):
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database(user_name, password)
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Users and Passwords',
    )

    parser.add_argument(
        '-u', '--user_name',
        type=str,
        help='Postgres Database user name',
        required=True,
    )

    parser.add_argument(
        '-p', '--password',
        type=str,
        help='Postgres Database password',
        required=True,
    )

    args = parser.parse_args()

    main(args.user_name, args.password)


