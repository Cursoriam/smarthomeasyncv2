import sqlite3

from .store_data_into_sqlite import conditioner_status_handler
DB_NAME = 'SmartHome.db'


TableSchema = """
drop table if exists CONDITIONER_DATA ;
create table CONDITIONER_DATA (
  id integer primary key autoincrement,
  ConditionerID text,
  Date_n_Time text,
  Status text
);
"""


def init_sqlite():
    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()

    sqlite3.complete_statement(TableSchema)
    curs.executescript(TableSchema)

    curs.close()
    conn.close()


__all__ = ['init_sqlite', 'conditioner_status_handler']
