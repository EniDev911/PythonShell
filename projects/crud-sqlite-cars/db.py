import sqlite3
from sqlite3 import Error
import os

CURDIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = "schema.sql"
FILE = os.path.join(CURDIR, "db", FILENAME)

def open_db():
    try:
        con = sqlite3.connect('cars.db')
        return con
    except Error as e:
        print('Error: ', e)

def run_query(sql, params='', multiple=False):
    with open_db() as con:
        cursor = con.cursor()
        try:
            if multiple:
                return cursor.executemany(sql, params)
            else:
                return cursor.execute(sql, params)
        except Error as e:
            print('Error: ', e)

def create_schema():
    with open(FILE, 'r') as sql_file:
        sql_script = sql_file.read()
        schema_created = run_query(sql_script)
        if schema_created.rowcount == -1:
            print("Database created successfully")

if __name__ == "__main__":
    create_schema()