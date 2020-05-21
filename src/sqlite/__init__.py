import sqlite3

from .store_data_into_sqlite import data_handler

DB_NAME = 'SmartHome.db'


CONDITIONER_TABLE_SCHEMA = """
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


LIGHT_TABLE_SCHEMA = """
drop table if exists LIGHT_DATA ;
create table if not exists LIGHT_DATA (
  id integer primary key autoincrement,
  LightID text,
  Date_n_Time text,
  Status boolean,
  Power integer,
  Mode text
);
"""


def init_sqlite() -> None:
    """
    Инициализация базы данных SQLite
    """
    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()

    sqlite3.complete_statement(CONDITIONER_TABLE_SCHEMA)
    curs.executescript(CONDITIONER_TABLE_SCHEMA)

    sqlite3.complete_statement(LIGHT_TABLE_SCHEMA)
    curs.executescript(LIGHT_TABLE_SCHEMA)

    curs.close()
    conn.close()


__all__ = ['init_sqlite', 'data_handler']
