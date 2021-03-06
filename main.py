import sys
import sqlite3
import csv_to_sqlite
import matplotlib.pyplot as plt

#Todo: .csv to .sqlite
def convertToSqlite( filename ):
    csv_name = filename + ".csv"
    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
    input_files = [csv_name]  # pto_ass in a list of CSV files
    csv_to_sqlite.write_csv(input_files, filename+".sqlite", options)
    return filename + ".sqlite"

# Todo: Differences diagram
def showDifference( result ):
    # 紅色破折號--, 藍色方塊bs ，綠色三角塊g^
    # plt.plot(x, x, 'r--', x, x ** 2, 'bs', x, x ** 3, 'g^')
    plt.show()
    return 0;

if __name__ == '__main__':
    print('Welcome to SQLiteHelper!')

    order_id = sys.argv[1]
    print("Testing: " + order_id)

    # Convert result to sqlite
    db_answer = convertToSqlite("answer")
    db_result = convertToSqlite("change_cd_idx")

    # Create a SQL connection to our SQLite database
    sql_answer = sqlite3.connect(db_answer)
    cursor_answer = sql_answer.cursor()

    # Attached 'db_result'
    CMD_ATTACH_RESULT = "ATTACH DATABASE ? AS vmc_result"
    cursor_answer.execute(CMD_ATTACH_RESULT, (db_result,))

    # Sum-up different rows from selection
    CMD_SELECT_DIFF = "SELECT ret.image_name, ret.change_feature, ans.change_feature " \
                      "FROM vmc_result.change_cd_idx ret, answer ans " \
                      "WHERE ret.image_name = ans.image_name " \
                      "and ret.change_feature!=ans.change_feature " \
                      "and ((ret.change_feature&1)|(ans.change_feature&1))"
    cursor_answer.execute(CMD_SELECT_DIFF)
    ret_diff = cursor_answer.fetchall()
    print(ret_diff)

    # Todo: Differences
    CMD_GET_COUNT = "SELECT ret.image_name, ret.change_feature, ans.change_feature " \
                    "FROM vmc_result.change_cd_idx ret, answer ans " \
                    "WHERE ret.image_name = ans.image_name "
    cursor_answer.execute(CMD_GET_COUNT)
    ret_total = cursor_answer.fetchall()

    total = len(ret_total);
    diff = len(ret_diff);
    print("Total: ?, diff: ?", (total, diff))

    # Todo: Download(wget) different results

    # Command
    # CMD_TABLE = "SELECT name FROM sqlite_master WHERE type='table';"
    # CMD_SELECT_ALL = "SELECT * FROM 'change_cd_idx'"
    # cursor_result.execute(CMD_SELECT_ALL)
    # for row in cursor_result:
    #     CMD_SELECT_DIFF = "SELECT * FROM 'answer'"
    #     print( row.image_name )
    # CMD_SELECT_DIFF = "SELECT d.image_name FROM 'change_cd_idx' d, 'answer' a "
    # cursor_result.execute(CMD_SELECT_DIFF)
    # print(cursor_result.fetchall())

    # Be sure to close the connection
    sql_answer.close()


