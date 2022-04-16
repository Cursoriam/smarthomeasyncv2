# TODO: Заменить создание на фабрику
from .data_parsers import temperature_data_parser
from .data_parsers import humidity_data_parser
from .data_parsers import heat_data_parser
from .utils import SqliteTableManager
from .db_managers import Sqlite3DBManager
from src.constants import TEMPERATURE_TABLE_NAME
from src.constants import HUMIDITY_TABLE_NAME
from src.constants import HEAT_TABLE_NAME
from src.constants import TEMPERATURE_TABLE_PARAMS
from src.constants import HUMIDITY_TABLE_PARAMS
from src.constants import HEAT_TABLE_PARAMS


db_manager = Sqlite3DBManager()  # Инициализация менеджера необходимой таблицы
table_manager = SqliteTableManager  # Инициализация менеджера необходимой таблицы


temperature_table_manager = table_manager(name=TEMPERATURE_TABLE_NAME, params=TEMPERATURE_TABLE_PARAMS,
                                          data_parser=temperature_data_parser)

humidity_table_manager = table_manager(name=HUMIDITY_TABLE_NAME, params=HUMIDITY_TABLE_PARAMS,
                                       data_parser=humidity_data_parser)

heat_table_manager = table_manager(name=HEAT_TABLE_NAME, params=HEAT_TABLE_PARAMS, data_parser=heat_data_parser)

