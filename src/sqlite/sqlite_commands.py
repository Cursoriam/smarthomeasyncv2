import sqlite3
from typing import List
from typing import Tuple
from typing import Union

from src.constants import DB_NAME


def create_table(table_statement: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()

    sqlite3.complete_statement(table_statement)
    curs.executescript(table_statement)

    curs.close()
    conn.close()


def execute_command(sql_query: str, args: Union[List, Tuple] = ()) -> None:
    conn = sqlite3.connect(DB_NAME)
    conn.execute('pragma foreign_keys = on')
    conn.commit()

    conn.cursor().execute(sql_query, args)
    conn.commit()

    conn.cursor().close()
    conn.close()


