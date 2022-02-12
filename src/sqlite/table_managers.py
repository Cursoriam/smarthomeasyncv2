from utils import TableManager
from src.constants import TEMPERATURE_TABLE_NAME
from src.constants import HUMIDITY_TABLE_NAME
from src.constants import CO2_TABLE_NAME

temperature_table_manager = TableManager(name=TEMPERATURE_TABLE_NAME)
temperature_table_manager.add_param("Temperature", "integer")

humidity_table_manager = TableManager(name=HUMIDITY_TABLE_NAME)
humidity_table_manager.add_param("Quantity", "real")

co2_table_manager = TableManager(name=CO2_TABLE_NAME)
co2_table_manager.add_param("Quantity", "real")
