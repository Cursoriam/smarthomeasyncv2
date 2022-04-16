# MQTT Settings
import os

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
KEEP_ALIVE_INTERVAL = 45

# Database params
DB_NAME = "SensorsData.db"

FIRST_KEY = "name"
SECOND_KEY = "type"

QUANTITY_OF_BASE_ELEMENTS = 2

TEMPERATURE_TABLE_NAME = "TEMPERATURE_DATA"
HUMIDITY_TABLE_NAME = "HUMIDITY_DATA"
HEAT_TABLE_NAME = "HEAT_DATA"

TEMPERATURE_TABLE_PARAMS = [{"name": 'Temperature', "type": 'integer'}, ]
HUMIDITY_TABLE_PARAMS = [{"name": 'Quantity', "type": 'real'}, ]
HEAT_TABLE_PARAMS = [{"name": 'Quantity', "type": 'real'}]


# JWT
JWT_SECRET = os.getenv('JWT_SECRET', 'mariya52')
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_MINUTES = 60

# Users Data
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'mariya52') + JWT_SECRET
