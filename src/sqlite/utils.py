from typing import List, Callable, Dict

from src.constants import QUANTITY_OF_BASE_ELEMENTS
from src.sqlite.sqlite_commands import execute_single_command


class TableManager:
    name: str
    params: List[Dict[str, str]]
    data_parser: Callable
    insert_command: str
    extract_all_command: str

    def __init__(self, name, params, data_parser):
        self.name = name
        self.params = params
        self.data_parser = data_parser
        self.insert_command = self.create_insert_command()
        self.extract_all_command = self.create_extract_all_command()

    def create_base_command(self):
        pass

    def create_insert_command(self) -> str:
        pass

    def extract_command(self, sensor_id: str):
        pass

    def create_extract_all_command(self) -> str:
        pass


class SqliteTableManager(TableManager):
    name: str
    params: List[Dict[str, str]]
    data_parser: Callable
    insert_command: str
    extract_all_command: str

    def __init__(self, name, params, data_parser):
        super().__init__(name, params, data_parser)

    def create_base_command(self):
        return """
            drop table if exists""" + self.name + """;
            create table if not exists""" + self.name + """ (
            id integer primary key autoincrement,
            Date_n_Time text,
            SensorId text,
            """ + ', '.join([f'{param["name"]} {param["type"]}' for param in self.params]) + " );"

    def create_insert_command(self):
        return "insert into " + self.name + " " + "(Date_n_Time, SensorId," + \
               ', '.join([f'{param["name"]}' for param in self.params]) + ") " +\
               "values (" + ','.join(['?' for i in range(QUANTITY_OF_BASE_ELEMENTS+len(self.params))]) + ")"

    def extract_command(self, sensor_id: str):
        return "SELECT * FROM " + self.name + " WHERE SensorId=" + sensor_id + " ORDER BY Date_n_Time DESC LIMIT 1"

    def create_extract_all_command(self):
        return "SELECT * FROM " + self.name


def handle_inserted_data(json_data: str, table_manager: SqliteTableManager):
    prepared_data = table_manager.data_parser(json_data)
    execute_single_command(table_manager.create_insert_command(), [prepared_data[key] for key in prepared_data])
    print("Insert " + table_manager.name + " in DB")


def handle_extracted_data(table_manager: TableManager, handled_data: list):
    records_data = [{"date_n_time": handled_data[1], "sensor_id": handled_data[2]}.update({param["name"]: record
                    for param in table_manager.params for record in handled_data[3:]})]  # тут возможен говняк сотоны
