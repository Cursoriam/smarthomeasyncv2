import sqlite3

from .store_data_into_sqlite import conditioner_status_handler

DB_NAME = 'SmartHome.db'


TABLE_SCHEMA = """
drop table if exists CONDITIONER_DATA ;
create table if not exists CONDITIONER_DATA (
  id integer primary key autoincrement,
  ConditionerID text,
  Date_n_Time text,
  Status boolean,
  Temperature integer,
  Mode text
);
"""


def init_sqlite() -> None:
    """
    Инициализация базы данных SQLite
    """
    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()

    sqlite3.complete_statement(TABLE_SCHEMA)
    curs.executescript(TABLE_SCHEMA)

    curs.close()
    conn.close()


__all__ = ['init_sqlite', 'conditioner_status_handler']
