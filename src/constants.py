# MQTT Settings
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
CO2_TABLE_NAME = "CO2_DATA"

TEMPERATURE_TABLE_PARAMS = [{"name": 'Temperature', "type": 'integer'},
                            ]
HUMIDITY_TABLE_PARAMS = [{"name": 'Quantity', "type": 'real'},
                         ]
CO2_TABLE_PARAMS = [{"name": 'Quantity', "type": 'real'}]

