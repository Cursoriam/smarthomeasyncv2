from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT
from src.sqlite import co2_table_manager
from .subscriber import on_message_for_db

userdata = {"mqtt_topic": "Classroom/CO2_Sensors", "table_manager": co2_table_manager, }


def co2_sensors_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "co2_sensors_client", userdata, on_message_for_db)
