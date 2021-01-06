import sqlite3

if __name__ == '__main__':
    print('Welcome to SQLiteHelper!')

    db_name = "Chinook_Sqlite_AutoIncrementPKs.sqlite"

    # Create a SQL connection to our SQLite database
    sql_connector = sqlite3.connect(db_name)
    cursor = sql_connector.cursor()

    # The result of a "cursor.execute" can be iterated over by row
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

    # Be sure to close the connection
    sql_connector.close()

