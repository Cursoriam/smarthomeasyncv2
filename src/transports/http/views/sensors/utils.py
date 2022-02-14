from src.sqlite import TableManager


def handle_data(table_manager: TableManager, records: list):
    records_data = [{"date_n_time": records[1], "sensor_id": records[2]}.update({param["name"]: record
                    for param in table_manager.params for record in records[3:]})] # тут возможен говняк сотоны
