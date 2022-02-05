import sqlite3
from src.constants import DB_NAME


def create_table(table_statement: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()

    sqlite3.complete_statement(table_statement)
    curs.executescript(table_statement)

    curs.close()
    conn.close()
