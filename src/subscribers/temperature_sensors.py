from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT
from src.sqlite import temperature_table_manager

userdata = {"mqtt_topic": "Classroom/Temperature_Sensors", "table_manager": temperature_table_manager, }


def temperature_sensors_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "temperature_sensors_client", userdata)
