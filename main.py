import sqlite3
import csv_to_sqlite

#Todo:
#.csv to .sqlite
def convertToSqlite():
    csv_name = "change_cd_idx.csv"
    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
    input_files = [csv_name]  # pass in a list of CSV files
    csv_to_sqlite.write_csv(input_files, "change_cd_idx.sqlite", options)
    return "change_cd_idx.sqlite"

if __name__ == '__main__':
    print('Welcome to SQLiteHelper!')

    # Convert result to sqlite
    db_answer = "Chinook_Sqlite_AutoIncrementPKs.sqlite"
    db_result = convertToSqlite()

    # Create a SQL connection to our SQLite database
    sql_answer = sqlite3.connect(db_answer)
    cursor_answer = sql_answer.cursor()

    sql_result = sqlite3.connect(db_result)
    cursor_result = sql_result.cursor()

    # The result of a "cursor.execute" can be iterated over by row
    cursor_answer.execute("SELECT * FROM sqlite_master WHERE type='table';")
    print(cursor_answer.fetchall())

    cursor_result.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor_result.fetchall())

    #
    cursor_result.execute("PRAGMA table_info('change_cd_idx')")
    print(cursor_result.fetchall())

    # Be sure to close the connection
    sql_answer.close()
    sql_result.close()


