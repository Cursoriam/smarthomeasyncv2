import sqlite3
from typing import List
from typing import Tuple
from typing import Union

from src.constants import DB_NAME


def execute_single_command(sql_query: str, args: Union[List, Tuple] = ()) -> sqlite3.Cursor:
    conn = sqlite3.connect(DB_NAME)
    conn.execute('pragma foreign_keys = on')
    conn.commit()

    result = conn.cursor().execute(sql_query, args)
    conn.commit()

    conn.cursor().close()
    conn.close()
    return result


def execute_multiple_commands(sqlite_statement: str) -> None:
    conn = sqlite3.connect(DB_NAME)

    sqlite3.complete_statement(sqlite_statement)
    conn.cursor().executescript(sqlite_statement)

    conn.cursor().close()
    conn.close()
