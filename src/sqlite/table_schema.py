def create_base_schema(table_name: str, table_params: str):
    return """
    drop table if exists""" + table_name + """;
    create table if not exists""" + table_name + """ (
    id integer primary key autoincrement,
    Date_n_Time text,
    SensorId text,
    """ + table_params
