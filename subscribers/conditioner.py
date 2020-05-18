from src.sqlite import conditioner_status_handler
import paho.mqtt.client as mqttc

# MQTT Settings
MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/Conditioner/Status"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK")
        client.subscribe(MQTT_Topic)
    else:
        print("Bad connection, RC = ", rc)


# Save Data into DB Table
def on_message(client, userdata, msg):
    # This is the Master Call for saving MQTT Data into DB
    # For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
    print("MQTT Data Received...")
    print("MQTT Topic: " + msg.topic)
    print("Data" + str(msg.payload))
    conditioner_status_handler(msg.topic, msg.payload)


def assign_callbacks_to_client(client):
    client.on_connect = on_connect
    client.on_message = on_message


def conditioner_subscribe():
    sub_clientA = mqttc.Client(client_id="clientgonnasubA")
    if not sub_clientA.is_connected():
        sub_clientA.connect_async(MQTT_Broker, MQTT_Port)
        assign_callbacks_to_client(sub_clientA)
        sub_clientA.loop_start()
