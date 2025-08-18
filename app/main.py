import paho.mqtt.client as mqtt

BROKER = "mosquitto"
PORT = 1883

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code", rc, flush=True)
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}", flush=True)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
