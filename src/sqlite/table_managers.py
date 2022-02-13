from data_parsers import temperature_data_parser
from data_parsers import humidity_data_parser
from data_parsers import co2_data_parser
from utils import TableManager
from src.constants import TEMPERATURE_TABLE_NAME
from src.constants import HUMIDITY_TABLE_NAME
from src.constants import CO2_TABLE_NAME

temperature_table_manager = TableManager(name=TEMPERATURE_TABLE_NAME, data_parser=temperature_data_parser)
temperature_table_manager.add_param("Temperature", "integer")

humidity_table_manager = TableManager(name=HUMIDITY_TABLE_NAME, data_parser=humidity_data_parser)
humidity_table_manager.add_param("Quantity", "real")

co2_table_manager = TableManager(name=CO2_TABLE_NAME, data_parser=co2_data_parser)
co2_table_manager.add_param("Quantity", "real")
