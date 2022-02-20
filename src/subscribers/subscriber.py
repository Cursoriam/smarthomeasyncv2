# pylint: disable=W0613, C0103
from typing import Any
from typing import Callable

import paho.mqtt.client as mqttc

from src.sqlite import handle_inserted_data
from src.sqlite import db_manager


def on_connect(client: mqttc, userdata: Any, flags: Any, rc: int) -> None:
    """
    Коллбэк подключения к брокеру
    :param client:
    :param userdata:
    :param flags:
    :param rc:
    """
    if rc == 0:
        print("Connected OK")
        client.subscribe(userdata["mqtt_topic"])
    else:
        print("Bad connection, RC = ", rc)


# Save Data into DB Table
def on_message_for_db(client: mqttc, userdata: Any, msg: mqttc.MQTTMessage) -> None:
    """
    Коллбэк получения сообщения
    :param client:
    :param userdata:
    :param msg:
    """
    # This is the Master Call for saving MQTT Data into DB
    # For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
    handle_inserted_data(msg.payload, userdata["table_manager"], db_manager)


def on_message_default(client: mqttc, userdata: Any, msg: mqttc.MQTTMessage) -> None:
    print("Data received: " + msg.payload.decode("utf-8"))


def broker_subscribe(mqtt_broker: str, mqtt_port: int, client_name: str, userdata: dict,
                     on_message_callback: Callable) -> None:
    """
    Метод подписки на топик
    """
    sub_client = mqttc.Client(client_id=client_name, userdata=userdata)
    if not sub_client.is_connected():
        sub_client.connect_async(mqtt_broker, mqtt_port)
        sub_client.on_connect = on_connect
        sub_client.on_message = on_message_callback
        sub_client.loop_start()
