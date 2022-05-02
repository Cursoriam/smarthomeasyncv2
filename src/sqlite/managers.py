# TODO: Refactor
from .data_parsers import temperature_data_parser
from .data_parsers import humidity_data_parser
from .data_parsers import heat_data_parser
from .utils import SqliteSensorsTableManager
from .utils import SqliteRecuperatorTableManager
from .db_managers import Sqlite3DBManager
from src.constants import SENSORS_DATA_DB_NAME
from src.constants import TEMPERATURE_TABLE_NAME
from src.constants import HUMIDITY_TABLE_NAME
from src.constants import HEAT_TABLE_NAME
from src.constants import TEMPERATURE_TABLE_PARAMS
from src.constants import HUMIDITY_TABLE_PARAMS
from src.constants import HEAT_TABLE_PARAMS
from src.constants import RECUPERATOR_DB_NAME
from src.constants import RECUPERATOR_SCHEDULE_TABLE_NAME


sensors_data_db_manager = Sqlite3DBManager(SENSORS_DATA_DB_NAME)  # Инициализация менеджера необходимой базы данных
sensors_data_table_manager = SqliteSensorsTableManager  # Инициализация менеджера необходимой таблицы

temperature_table_manager = sensors_data_table_manager(name=TEMPERATURE_TABLE_NAME, params=TEMPERATURE_TABLE_PARAMS,
                                                       data_parser=temperature_data_parser)
humidity_table_manager = sensors_data_table_manager(name=HUMIDITY_TABLE_NAME, params=HUMIDITY_TABLE_PARAMS,
                                                    data_parser=humidity_data_parser)
heat_table_manager = sensors_data_table_manager(name=HEAT_TABLE_NAME, params=HEAT_TABLE_PARAMS,
                                                data_parser=heat_data_parser)

recuperator_data_db_manager = Sqlite3DBManager(RECUPERATOR_DB_NAME)
recuperator_data_table_manager = SqliteRecuperatorTableManager

recuperator_schedule_manager = recuperator_data_table_manager(name=RECUPERATOR_SCHEDULE_TABLE_NAME,
                                                              params=None, data_parser=None)
