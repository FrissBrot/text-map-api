from config import DB_CONFIG
from dbconnection import table_exists, execute_sql_script, test_connection

def setup():
    print("setup")
    print(DB_CONFIG)
    print(test_connection("SELECT * FROM \"public\".chunk;"))

    if table_exists("chunk"):
        print("Tabelle existiert")
    else:
        execute_sql_script("/sql/setup.sql")