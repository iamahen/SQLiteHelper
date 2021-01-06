import sqlite3
import csv_to_sqlite

#Todo:
#.csv to .sqlite
def convertToSqlite():
    csv_name = "data.csv"
    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
    input_files = [csv_name]  # pass in a list of CSV files
    csv_to_sqlite.write_csv(input_files, "output.sqlite", options)

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

