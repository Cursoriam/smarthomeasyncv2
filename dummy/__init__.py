import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

# ====================================================
# MQTT Settings
MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/Conditioner/Status"


# ====================================================

def on_connect(mqttc, userdata, flags, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_disconnect(mqttc, userdata, flags, rc):
    if rc != 0:
        pass


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.connect_async(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.loop_start()


def publish_To_Topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))

# ====================================================
# FAKE SENSOR
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker


toggle = 0


def publish_Fake_Sensor_Values_to_MQTT():
    threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
    global toggle
    if toggle == 0:
        Conditioner_Fake_Status = bool(random.getrandbits(1))
        Conditioner_Fake_Id = str(random.randrange(1, 3))
        Modes = ['Easy', 'Normal', 'Hard']
        Conditioner_Fake_Mode = Modes[random.randrange(0, 2)]
        if not Conditioner_Fake_Status:
            Conditioner_Fake_Mode = 'Off'
        Conditioner_Fake_Temperature = random.randrange(-50, 50)

        Humidity_Data = {'ConditionerID': Conditioner_Fake_Id, 'Date': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
                         'Status': Conditioner_Fake_Status, 'Temperature': Conditioner_Fake_Temperature, 'Mode': Conditioner_Fake_Mode}
        humidity_json_data = json.dumps(Humidity_Data)

        print("Publishing fake Humidity Value: " + str(Conditioner_Fake_Status) + "...")
        publish_To_Topic(MQTT_Topic, humidity_json_data)


publish_Fake_Sensor_Values_to_MQTT()
