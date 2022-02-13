from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT
from src.sqlite import humidity_table_manager

userdata = {"mqtt_topic": "Classroom/Humidity_Sensors", "table_manager": humidity_table_manager, }


def humidity_sensors_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "humidity_sensors_client", userdata)
