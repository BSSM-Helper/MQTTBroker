from core.MQTTClient import MQTTClient

BROKER = "mosquitto"
PORT = 1883

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code", rc, flush=True)
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}", flush=True)

client = MQTTClient(on_connect, on_message, BROKER, PORT)
