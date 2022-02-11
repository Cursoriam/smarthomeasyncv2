from src.constants import BASE_TABLE_SCHEMA


class BaseSchema:
    schema: str = """
    drop table if exists TEMPERATURE_DATA ;
    create table if not exists TEMPERATURE_DATA (
    id integer primary key autoincrement,
    Date_n_Time text,
    SensorId text,
    """


class TemperatureSchema(BaseSchema):
    schema = super().schema + "Temperature integer );"


class HumiditySchema(BaseSchema):
    schema = super().schema + "Quantity real );"


class C02Schema(BaseSchema):
    schema = super().schema + "Quantity real );"
