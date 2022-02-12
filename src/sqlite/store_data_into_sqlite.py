# TODO:
import json
import sqlite3
from typing import List
from typing import Tuple
from typing import Union
from typing import Callable

from src.constants import DB_NAME


def execute_command(sql_query: str, args: Union[List, Tuple] = ()) -> None:
    conn = sqlite3.connect(DB_NAME)
    conn.execute('pragma foreign_keys = on')
    conn.commit()

    conn.cursor().execute(sql_query, args)
    conn.commit()

    conn.cursor().close()
    conn.close()


def handle_data(self, json_data: str, table_insert_command: str, parse_data: Callable, data_name: str):
    parsed_data = parse_data(json_data)
    DatabaseManager.execute_command(table_insert_command, [data for data in parsed_data])
    print("Insert " + data_name + " in DB")
