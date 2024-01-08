
import sqlite3
from sqlite3 import Error
import server.config as config


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(config.DB_FILE)
        return conn
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

conn = create_connection()