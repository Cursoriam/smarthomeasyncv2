from typing import List, Callable

from src.constants import QUANTITY_OF_BASE_ELEMENTS
from src.sqlite.sqlite_commands import execute_command


class TableManager:
    name: str
    params: List[dict]
    data_parser: Callable

    def __init__(self, name, data_parser):
        self.name = name
        self.data_parser = data_parser

    def create_base_schema(self):
        return """
            drop table if exists""" + self.name + """;
            create table if not exists""" + self.name + """ (
            id integer primary key autoincrement,
            Date_n_Time text,
            SensorId text,
            """ + ', '.join([f'{param["name"]} {param["type"]}' for param in self.params]) + " );"

    def insert_command(self):
        return "insert into " + self.name + " " + "(Data_n_Time, SensorId," + \
               ', '.join([f'{param["name"]}' for param in self.params]) + ") " +\
               "values (" + ','.join(['?' for i in range(QUANTITY_OF_BASE_ELEMENTS+len(self.params))]) + ")"

    def add_param(self, param_name: str, param_type: str):
        self.params.append({"name": param_name, "type": param_type})


def handle_data(json_data: str, table_manager: TableManager):
    prepared_data = table_manager.data_parser(json_data)
    execute_command(table_manager.insert_command(), [prepared_data[key] for key in prepared_data])
    print("Insert " + table_manager.name + " in DB")
