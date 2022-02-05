# Возможна, реализация наследования

# В таблице TEMPERATURE_DATA хранятся показания температуры, полученные от датчиков.
TEMPERATURE_TABLE_SCHEMA = """
drop table if exists TEMPERATURE_DATA ;
create table if not exists TEMPERATURE_DATA (
    id integer primary key autoincrement,
    Temperaure integer,
    Date_n_Time text,
    SensorId text
);
"""

HUMIDITY_TABLE_SCHEMA = """
drop table if exists HUMIDITY_DATA ;
create table if not exists HUMIDIDTY_DATA (
    id integer primary key autoincrement,
    Quantity real,
    Date_n_Time text,
    SensorId text 
);
"""

CO2_TABLE_SCHEMA = """
drop table if exists CO2_DATA ;
create table if not exists CO2_DATA (
    id integer primary key autoincrement,
    Quantity real,
    Date_n_Time text,
    SensorId text
);
"""