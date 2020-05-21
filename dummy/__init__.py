from typing import Any

import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
KEEP_ALIVE_INTERVAL = 45
MQTT_CONDITIONER_TOPIC = "Home/Conditioner"
MQTT_LIGHT_TOPIC = "Home/Light"

MODES = ['Easy', 'Normal', 'Hard']


def on_connect(mqttc: mqtt, userdata: Any, flags: Any, rc: int):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_BROKER))


def on_disconnect(mqttc: mqtt, userdata: Any, flags: Any, rc: int):
    if rc != 0:
        pass


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.connect_async(MQTT_BROKER, int(MQTT_PORT), int(KEEP_ALIVE_INTERVAL))
mqttc.loop_start()


def publish_to_topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))


toggle = 0


def publish_fake_sensor_values_to_mqtt():
    threading.Timer(3.0, publish_fake_sensor_values_to_mqtt).start()
    global toggle
    if toggle == 0:
        conditioner_fake_status = bool(random.getrandbits(1))
        conditioner_fake_id = str(random.randrange(1, 3))
        conditioner_fake_mode = MODES[random.randrange(0, 2)]
        if not conditioner_fake_status:
            conditioner_fake_mode = 'Off'
        conditioner_fake_temperature = random.randrange(-50, 50)

        conditioner_data = {'ConditionerID': conditioner_fake_id,
                            'Date': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
                            'Status': conditioner_fake_status,
                            'Temperature': conditioner_fake_temperature,
                            'Mode': conditioner_fake_mode}
        conditioner_json_data = json.dumps(conditioner_data)

        print("Publishing fake Conditioner Value: " + str(conditioner_fake_status) + "...")
        publish_to_topic(MQTT_CONDITIONER_TOPIC, conditioner_json_data)
        toggle = 1
    else:
        light_fake_status = bool(random.getrandbits(1))
        light_fake_id = str(random.randrange(1, 3))
        light_fake_mode = MODES[random.randrange(0, 2)]
        if not light_fake_status:
            light_fake_mode = 'Off'
        light_fake_power = random.randrange(1, 14)

        light_data = {'LightID': light_fake_id,
                      'Date': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
                      'Status': light_fake_status,
                      'Mode': light_fake_mode,
                      'Power': light_fake_power}

        light_json_data = json.dumps(light_data)

        print("Publishing fake Light Value: " + str(light_fake_status) + "...")
        publish_to_topic(MQTT_LIGHT_TOPIC, light_json_data)
        toggle = 0


publish_fake_sensor_values_to_mqtt()
