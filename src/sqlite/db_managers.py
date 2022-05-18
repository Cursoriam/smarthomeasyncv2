import sqlite3
from typing import List
from typing import Tuple
from typing import Union


class DBManager:

    def execute_single_command(self, query: str, args: Union[List, Tuple] = ()):
        pass

    def execute_multiple_commands(self, query: str):
        pass


class Sqlite3DBManager(DBManager):
    connection: sqlite3.Connection

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)

    def __del__(self):
        self.connection.cursor().close()
        self.connection.close()

    def execute_single_command(self, sql_query: str, args: Union[List, Tuple] = ()) -> sqlite3.Cursor:
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()

        result = self.connection.cursor().execute(sql_query, args)
        self.connection.commit()

        return result

    def execute_multiple_commands(self, sql_query: str) -> None:
        sqlite3.complete_statement(sql_query)
        self.connection.cursor().executescript(sql_query)

