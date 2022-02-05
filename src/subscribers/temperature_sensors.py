from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT

userdata = {"mqtt_topic": "Classroom/Temperature_Sensors"}


def temperature_sensors_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "temperature_sensors_client", userdata)
